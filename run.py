from flask import jsonify
"""A  module to run the application"""
from app import create_app
from instance import config

app = create_app(config.DevelopmentConfig)


@app.route('/', methods=['GET'])
def home():
    return(jsonify({
        "status": 200,
        "data": [{
            "message": "Welcome to politico API, Remember This is An API checkout list of available endpoints ",
            "Available endpoints on this git hub repo README file": "https://github.com/OCHIENGDAVIS/pols-with-datastructures"
        }]
    }))


if __name__ == '__main__':
    app.run()
