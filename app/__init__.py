"""creates an instance of a flask application and runs it"""
from flask import Flask


def create_app(config_file):
    app = Flask(__name__)
    app.config.from_object(config_file)
    from app.api.v1.views.routes import api
    app.register_blueprint(api, url_prefix='/api/v1')
    return app
