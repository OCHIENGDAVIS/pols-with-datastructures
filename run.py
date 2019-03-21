"""A  module to run the application"""
from app import create_app
from instance import config

app = create_app(config.DevelopmentConfig)


if __name__ == '__main__':
    app.run()
