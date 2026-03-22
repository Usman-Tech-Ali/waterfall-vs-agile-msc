from datetime import date
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    # Relationships
    created_tasks = db.relationship('Task', foreign_keys='Task.creator_id', backref='creator', lazy='dynamic')
    assigned_tasks = db.relationship('Task', foreign_keys='Task.assignee_id', backref='assignee', lazy='dynamic')
    notifications = db.relationship('Notification', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def unread_notification_count(self):
        return self.notifications.filter_by(is_read=False).count()

    def __repr__(self):
        return f'<User {self.username}>'


class Task(db.Model):
    __tablename__ = 'task'

    STATUS_OPTIONS = ['To Do', 'In Progress', 'Done']
    PRIORITY_OPTIONS = ['Low', 'Medium', 'High']
    CATEGORY_OPTIONS = ['Work', 'Personal', 'Urgent']  # CR-001

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    priority = db.Column(db.String(10), nullable=False, default='Medium')
    status = db.Column(db.String(20), nullable=False, default='To Do')
    category = db.Column(db.String(20), nullable=True, default='Work')  # CR-001
    due_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    assignee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relationships
    notifications = db.relationship('Notification', backref='task', lazy='dynamic')
    comments = db.relationship('Comment', backref='task', lazy='dynamic', order_by='Comment.created_at')  # CR-003

    @property
    def is_overdue(self):
        return self.due_date < date.today() and self.status != 'Done'

    def __repr__(self):
        return f'<Task {self.title}>'


class Notification(db.Model):
    __tablename__ = 'notification'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=True)
    message = db.Column(db.String(255), nullable=False)
    is_read = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f'<Notification {self.id} for user {self.user_id}>'


class Comment(db.Model):  # CR-003
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f'<Comment {self.id} on task {self.task_id}>'
