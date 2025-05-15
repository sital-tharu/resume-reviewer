# __init__.py initializes the Flask app and registers blueprints
from flask import Flask
from .routes import app as app_blueprint  # Import the blueprint from routes.py

def create_app():
    """
    Factory function to create and configure the Flask app instance.
    Registers blueprints and sets configuration variables.
    """
    app = Flask(__name__)
    app.register_blueprint(app_blueprint)  # Register the main blueprint
    app.config['UPLOAD_FOLDER'] = 'uploads'  # Set the upload folder
    return app