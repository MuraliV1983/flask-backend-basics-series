import os
from flask import Flask
from .config import Config
from .extensions import db
from .controllers.user_controller import user_bp
from sqlalchemy_utils import database_exists, create_database

def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__, template_folder=os.path.join(basedir, 'views', 'templates'))
    app.config.from_object(Config)

    if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
        create_database(app.config["SQLALCHEMY_DATABASE_URI"])

    db.init_app(app)
    app.register_blueprint(user_bp)

    with app.app_context():
        db.create_all()

    return app
