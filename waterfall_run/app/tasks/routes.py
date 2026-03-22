from datetime import date, datetime
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .. import db
from ..models import Task, User, Notification, Comment

tasks_bp = Blueprint('tasks', __name__)


def _create_notification(user_id, message, task_id=None):
    notif = Notification(user_id=user_id, message=message, task_id=task_id)
    db.session.add(notif)


@tasks_bp.route('/')
@login_required
def index():
    return redirect(url_for('tasks.dashboard'))


@tasks_bp.route('/dashboard')
@login_required
def dashboard():
    today = date.today()
    assigned = Task.query.filter_by(assignee_id=current_user.id).order_by(Task.due_date).all()
    overdue_count = sum(1 for t in assigned if t.is_overdue)

    # CR-002: status counts
    status_counts = {
        'To Do': sum(1 for t in assigned if t.status == 'To Do'),
        'In Progress': sum(1 for t in assigned if t.status == 'In Progress'),
        'Done': sum(1 for t in assigned if t.status == 'Done'),
    }

    unread_notifications = (
        current_user.notifications
        .filter_by(is_read=False)
        .order_by(Notification.created_at.desc())
        .limit(5)
        .all()
    )

    return render_template(
        'tasks/dashboard.html',
        tasks=assigned,
        overdue_count=overdue_count,
        status_counts=status_counts,
        notifications=unread_notifications,
        today=today,
    )


@tasks_bp.route('/tasks')
@login_required
def task_list():
    status_filter = request.args.get('status', '')
    priority_filter = request.args.get('priority', '')

    query = Task.query
    if status_filter:
        query = query.filter_by(status=status_filter)
    if priority_filter:
        query = query.filter_by(priority=priority_filter)

    tasks = query.order_by(Task.due_date).all()
    return render_template(
        'tasks/task_list.html',
        tasks=tasks,
        status_filter=status_filter,
        priority_filter=priority_filter,
        status_options=Task.STATUS_OPTIONS,
        priority_options=Task.PRIORITY_OPTIONS,
    )


@tasks_bp.route('/tasks/create', methods=['GET', 'POST'])
@login_required
def create_task():
    users = User.query.order_by(User.username).all()

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        assignee_id = request.form.get('assignee_id', type=int)
        due_date_str = request.form.get('due_date', '')
        priority = request.form.get('priority', 'Medium')
        category = request.form.get('category', 'Work')  # CR-001

        error = None
        if not title:
            error = 'Title is required.'
        elif not assignee_id:
            error = 'Assignee is required.'
        elif not due_date_str:
            error = 'Due date is required.'
        elif priority not in Task.PRIORITY_OPTIONS:
            error = 'Invalid priority.'
        elif category not in Task.CATEGORY_OPTIONS:
            error = 'Invalid category.'

        if not error:
            try:
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
            except ValueError:
                error = 'Invalid date format.'

        if error:
            flash(error, 'danger')
        else:
            task = Task(
                title=title,
                description=description,
                assignee_id=assignee_id,
                due_date=due_date,
                priority=priority,
                category=category,
                creator_id=current_user.id,
            )
            db.session.add(task)
            db.session.flush()  # get task.id before commit

            # Notify assignee (unless they're the creator)
            if assignee_id != current_user.id:
                _create_notification(
                    assignee_id,
                    f'You have been assigned a new task: "{title}"',
                    task_id=task.id,
                )

            db.session.commit()
            flash('Task created successfully.', 'success')
            return redirect(url_for('tasks.dashboard'))

    return render_template(
        'tasks/create_task.html',
        users=users,
        priority_options=Task.PRIORITY_OPTIONS,
        category_options=Task.CATEGORY_OPTIONS,
    )


@tasks_bp.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    users = User.query.order_by(User.username).all()

    if request.method == 'POST':
        # Handle comment submission (CR-003)
        if 'comment_body' in request.form:
            body = request.form.get('comment_body', '').strip()
            if body:
                comment = Comment(task_id=task.id, author_id=current_user.id, body=body)
                db.session.add(comment)
                db.session.commit()
                flash('Comment added.', 'success')
            return redirect(url_for('tasks.edit_task', task_id=task.id))

        # Handle task edit
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        assignee_id = request.form.get('assignee_id', type=int)
        due_date_str = request.form.get('due_date', '')
        priority = request.form.get('priority', 'Medium')
        category = request.form.get('category', 'Work')  # CR-001
        new_status = request.form.get('status', task.status)

        error = None
        if not title:
            error = 'Title is required.'
        elif not assignee_id:
            error = 'Assignee is required.'
        elif not due_date_str:
            error = 'Due date is required.'

        if not error:
            try:
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
            except ValueError:
                error = 'Invalid date format.'

        if error:
            flash(error, 'danger')
        else:
            old_assignee_id = task.assignee_id
            old_status = task.status

            task.title = title
            task.description = description
            task.due_date = due_date
            task.priority = priority
            task.category = category

            # Notify on reassignment
            if assignee_id != old_assignee_id:
                task.assignee_id = assignee_id
                if assignee_id != current_user.id:
                    _create_notification(
                        assignee_id,
                        f'You have been assigned task: "{title}"',
                        task_id=task.id,
                    )

            # Notify on status change
            if new_status != old_status and new_status in Task.STATUS_OPTIONS:
                task.status = new_status
                if task.assignee_id != current_user.id:
                    _create_notification(
                        task.assignee_id,
                        f'Task "{title}" status changed to "{new_status}"',
                        task_id=task.id,
                    )

            db.session.commit()
            flash('Task updated.', 'success')
            return redirect(url_for('tasks.dashboard'))

    return render_template(
        'tasks/edit_task.html',
        task=task,
        users=users,
        priority_options=Task.PRIORITY_OPTIONS,
        status_options=Task.STATUS_OPTIONS,
        category_options=Task.CATEGORY_OPTIONS,
    )
