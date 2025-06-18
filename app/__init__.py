from flask import Flask
from .config import Config

# Create a new Flask application instance
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .routes import main
    app.register_blueprint(main)

    return app
