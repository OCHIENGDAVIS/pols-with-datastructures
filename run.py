"""A  module to run the application"""
from app import create_app
from instance import config
from flask import jsonify
app = create_app(config.DevelopmentConfig)


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the app"
    })


if __name__ == '__main__':

    app.run(debug=True)
