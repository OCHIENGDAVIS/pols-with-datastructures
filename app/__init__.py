"""creates an instance of a flask application and runs it"""
from flask import Flask
from app.api.v1.views.routes import not_found_error, bad_request
from app.api.v1.views.routes import api


def create_app(config_file):
    """Creates an instance of a flask app"""
    app = Flask(__name__)
    app.config.from_object(config_file)
    app.register_blueprint(api, url_prefix='/api/v1')
    app.register_error_handler(404, not_found_error)
    app.register_error_handler(400, bad_request)
    return app
