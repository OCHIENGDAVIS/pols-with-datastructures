from flask import Flask
from instance import config


def create_app(config_file):
    app = Flask(__name__)
    app.config.from_object(config_file)
    from app.api.v1.main import api
    app.register_blueprint(api, url_prefix='/api/v1')
    return  app


if __name__ == '__main__':
    app = create_app(config)
    app.run()



