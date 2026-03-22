import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'warning'


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Ensure instance folder exists (one level up from app package, at waterfall_run/)
    instance_path = os.path.join(os.path.dirname(app.root_path), 'instance')
    os.makedirs(instance_path, exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from .auth.routes import auth_bp
    from .tasks.routes import tasks_bp
    from .notifications.routes import notifications_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(notifications_bp)

    with app.app_context():
        db.create_all()

    return app
