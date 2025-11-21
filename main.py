from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create database instance at module level so models can import it
db = SQLAlchemy()

def create_app():
    
    # Creating the flask app object - this is the core of our app!
    app = Flask(__name__)

    # configuring our app:
    app.config.from_object("config.app_config")

    # Initialise the database with the app
    db.init_app(app)
    
    return app