from flask import Blueprint, jsonify
from app.api.v1.views.party import Party


api = Blueprint('api', __name__)


@api.route('/parties', methods = ['GET'])
def get_all_parties():
    parties = Party.get_all_parties()
    return jsonify(parties)



@api.route('/parties', methods = ['POST'])
def create_a_party():
    pass

@api.route('/parties/<int:id>', methods = ['GET'])
def get_a_party(id):
    pass

@api.route('/parties/<int:id>', methods = ['DELETE'])
def delete_a_party(id):
    pass

@api.route('/parties/<int:id>', methods = ['PATCH'])
def edit_a_party(id):
    pass

@api.route('/offices', methods = ['GET'])
def get_all_offices():
    pass

@api.route('/offices', methods = ['POST'])
def create_an_office():
    pass

@api.route('/offices/<int:id>', methods = ['GET'])
def get_an_office():
    pass

