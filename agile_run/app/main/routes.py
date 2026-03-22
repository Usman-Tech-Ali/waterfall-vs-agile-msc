from datetime import datetime, date
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from . import main_bp
from .. import db
from ..models import User, Task, Notification, Comment


def create_notification(user_id, message, task_id=None):
    """Helper function to create notifications"""
    notification = Notification(
        user_id=user_id,
        message=message,
        task_id=task_id
    )
    db.session.add(notification)


@main_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return redirect(url_for('auth.login'))


@main_bp.route('/dashboard')
@login_required
def dashboard():
    # Get user's assigned tasks
    tasks = current_user.assigned_tasks.order_by(Task.due_date).all()
    
    # Calculate status counts
    status_counts = {
        'To Do': sum(1 for t in tasks if t.status == 'To Do'),
        'In Progress': sum(1 for t in tasks if t.status == 'In Progress'),
        'Done': sum(1 for t in tasks if t.status == 'Done'),
        'Overdue': sum(1 for t in tasks if t.is_overdue)
    }
    
    # Get recent unread notifications
    notifications = current_user.get_unread_notifications().limit(5).all()
    
    return render_template('main/dashboard.html', 
                         tasks=tasks, 
                         status_counts=status_counts,
                         notifications=notifications)


@main_bp.route('/tasks')
@login_required
def task_list():
    # Get filter parameters
    status_filter = request.args.get('status', '')
    priority_filter = request.args.get('priority', '')
    
    # Build query
    query = Task.query
    
    if status_filter:
        query = query.filter(Task.status == status_filter)
    if priority_filter:
        query = query.filter(Task.priority == priority_filter)
    
    tasks = query.order_by(Task.due_date).all()
    
    return render_template('main/task_list.html', 
                         tasks=tasks,
                         status_filter=status_filter,
                         priority_filter=priority_filter,
                         status_choices=Task.STATUS_CHOICES,
                         priority_choices=Task.PRIORITY_CHOICES)


@main_bp.route('/tasks/create', methods=['GET', 'POST'])
@login_required
def create_task():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        assignee_id = request.form.get('assignee_id', type=int)
        due_date_str = request.form.get('due_date', '')
        priority = request.form.get('priority', 'Medium')
        category = request.form.get('category', 'Work')
        
        # Validation
        if not title or not assignee_id or not due_date_str:
            flash('Title, assignee, and due date are required.', 'error')
            return render_template('main/create_task.html', users=User.query.all())
        
        try:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
        except ValueError:
            flash('Invalid date format.', 'error')
            return render_template('main/create_task.html', users=User.query.all())
        
        # Create task
        task = Task(
            title=title,
            description=description,
            assignee_id=assignee_id,
            due_date=due_date,
            priority=priority,
            category=category,
            creator_id=current_user.id
        )
        
        db.session.add(task)
        db.session.flush()  # Get task ID
        
        # Create notification for assignee (if not self-assigned)
        if assignee_id != current_user.id:
            create_notification(
                assignee_id,
                f'You have been assigned a new task: "{title}"',
                task.id
            )
        
        db.session.commit()
        flash('Task created successfully!', 'success')
        return redirect(url_for('main.dashboard'))
    
    users = User.query.order_by(User.username).all()
    return render_template('main/create_task.html', users=users)


@main_bp.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    if request.method == 'POST':
        # Handle comment submission
        if 'comment_body' in request.form:
            comment_body = request.form.get('comment_body', '').strip()
            if comment_body:
                comment = Comment(
                    body=comment_body,
                    task_id=task.id,
                    author_id=current_user.id
                )
                db.session.add(comment)
                db.session.commit()
                flash('Comment added successfully!', 'success')
            return redirect(url_for('main.edit_task', task_id=task.id))
        
        # Handle task update
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        assignee_id = request.form.get('assignee_id', type=int)
        due_date_str = request.form.get('due_date', '')
        priority = request.form.get('priority', 'Medium')
        category = request.form.get('category', 'Work')
        status = request.form.get('status', task.status)
        
        # Validation
        if not title or not assignee_id or not due_date_str:
            flash('Title, assignee, and due date are required.', 'error')
            return render_template('main/edit_task.html', task=task, users=User.query.all())
        
        try:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
        except ValueError:
            flash('Invalid date format.', 'error')
            return render_template('main/edit_task.html', task=task, users=User.query.all())
        
        # Track changes for notifications
        old_assignee_id = task.assignee_id
        old_status = task.status
        
        # Update task
        task.title = title
        task.description = description
        task.assignee_id = assignee_id
        task.due_date = due_date
        task.priority = priority
        task.category = category
        task.status = status
        task.updated_at = datetime.utcnow()
        
        # Create notifications for changes
        if assignee_id != old_assignee_id and assignee_id != current_user.id:
            create_notification(
                assignee_id,
                f'You have been assigned task: "{title}"',
                task.id
            )
        
        if status != old_status and task.assignee_id != current_user.id:
            create_notification(
                task.assignee_id,
                f'Task "{title}" status changed to "{status}"',
                task.id
            )
        
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('main.dashboard'))
    
    users = User.query.order_by(User.username).all()
    return render_template('main/edit_task.html', task=task, users=users)


@main_bp.route('/notifications')
@login_required
def notifications():
    notifications = current_user.notifications.order_by(Notification.created_at.desc()).all()
    return render_template('main/notifications.html', notifications=notifications)


@main_bp.route('/notifications/<int:notification_id>/mark_read', methods=['POST'])
@login_required
def mark_notification_read(notification_id):
    notification = Notification.query.get_or_404(notification_id)
    if notification.user_id == current_user.id:
        notification.is_read = True
        db.session.commit()
    return redirect(request.referrer or url_for('main.notifications'))


@main_bp.route('/notifications/mark_all_read', methods=['POST'])
@login_required
def mark_all_notifications_read():
    current_user.notifications.filter_by(is_read=False).update({'is_read': True})
    db.session.commit()
    flash('All notifications marked as read.', 'success')
    return redirect(url_for('main.notifications'))