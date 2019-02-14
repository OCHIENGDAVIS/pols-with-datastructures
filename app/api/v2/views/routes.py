from flask import Blueprint
from flask import jsonify
api2 = Blueprint("api2", __name__)


@api2.route('/parties')
def get_all_parties_2():
    return jsonify({'message': "things are realy good"})
