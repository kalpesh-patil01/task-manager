from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_login import LoginManager
from config import Config  # get the settings in config.py

# initialization of Plugins  
db = SQLAlchemy()
socketio = SocketIO()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # load the all settings in config.py 
    app.config.from_object(Config)

    # initialize Plugins  
    db.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*")
    login_manager.init_app(app)
    
    # handeled login required pages 
    login_manager.login_view = 'auth.login'

    # register all routers blueprint
    from .routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .routes.tasks import tasks as tasks_blueprint
    app.register_blueprint(tasks_blueprint)

    from .routes.analytics import analytics as analytics_blueprint
    app.register_blueprint(analytics_blueprint)

    #Db table create 
    with app.app_context():
        from . import models  # load the table structure 
        db.create_all()       # create the tables from PostgreSQL 

    return app