from flask import Flask
from .routes import app as app_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(app_blueprint)
    app.config['UPLOAD_FOLDER'] = 'uploads'
    return app