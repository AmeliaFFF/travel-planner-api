from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    """Creates and configures the Flask application instance. Initialises extensions, registers blueprints for all controllers, and sets up global error handlers."""
    app = Flask(__name__)
    app.config.from_object("config.app_config")

    db.init_app(app)
    ma.init_app(app)

    from commands import db_commands
    app.register_blueprint(db_commands)

    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)
    
    @app.errorhandler(400)
    def handle_400(err):
        return jsonify({
            "error": "Bad request.", 
            "details": str(err)
            }), 400

    @app.errorhandler(404)
    def handle_404(err):
        return jsonify({
            "error": "Not found.",
            "details": "The requested URL or resource does not exist."
            }), 404

    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        return jsonify({
            "error": "Validation failed.",
            "messages": err.messages
            }), 400

    return app