from  flask import jsonify, request
from flask import Blueprint
from app.api.v1.models.party_model import Party, parties
from app.api.v1.utils import validate_party_info, find_by_id



api = Blueprint('api', __name__)


@api.route('/parties', methods = ['GET'])
def get_all_parties():
    all_parties = Party.get_all_parties()
    return jsonify(all_parties), 200


@api.route('/parties', methods = ['POST'])
def create_a_party():
    data = request.get_json()
    validation_response = validate_party_info(data)
    if validation_response is None:
        new_party = Party.create_party(data['id'], data['name'], data['hqAddress'], data['logoUrl'])
        return jsonify({
            "status": 201,
            "data": [
                {
                    "id": new_party["id"],
                    "name": new_party["name"]
                },
            ]
        }), 201
    else:
        return jsonify({"message":validation_response['message']}), validation_response['code']



@api.route('/parties/<int:party_id>', methods = ['GET'])
def get_a_party(party_id):
    if not isinstance(party_id, int):
        return jsonify({"message": "id must be an integer"}), 400
    elif party_id < 0:
        return jsonify({"message": "Id can not be a negative"}), 400
    else:
        for party in parties:
            if party['id'] == party_id:
                return jsonify(party), 200
        return jsonify({"message":"party do not exists"}), 404


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

