from flask import Flask
from .routes import main, admin


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('../config.py')

    # Registrar blueprints (rotas)
    app.register_blueprint(main)
    app.register_blueprint(admin)

    return app