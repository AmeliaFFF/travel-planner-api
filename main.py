from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialise SQLAlchemy and Marshmallow objects:
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    
    # Creating the flask app object - this is the core of our app!
    app = Flask(__name__)

    # configuring our app:
    app.config.from_object("config.app_config")

    # Initialise the database with the app:
    db.init_app(app)

    # Initialise Marshmallow with the app:
    ma.init_app(app)

    from commands import db_commands
    app.register_blueprint(db_commands)

    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)
    
    return app