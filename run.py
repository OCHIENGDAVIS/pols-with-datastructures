"""A  module to run the application"""
from app import create_app
from instance import config
from flask import jsonify


@app.route("/")
def home():
    return jsonify({
        "message": "welcome to politico REST API, to get started add the url prefix /api/v1 to every endpoint"
    })


if __name__ == '__main__':
    app = create_app(config.DevelopmentConfig)
    app.run(debug=True)
