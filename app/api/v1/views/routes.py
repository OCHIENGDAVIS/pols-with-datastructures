from flask import jsonify, request
from flask import Blueprint
"""Module for handling requests and request routings"""
from app.api.v1.models.party_models import Party, parties
from app.api.v1.models.office_models import Office, offices
from app.api.v1.utils import validate_party_info, find_item_by_id

api = Blueprint('api', __name__)


@api.route('/parties', methods=['GET'])
def get_all_parties():
    """Gets all parties"""
    data = []
    for party in parties:
        temp_party = {
            "id": party["id"],
            "name": party["name"],
            "hqAddress": party["hqAddress"],
            "logoUrl": party["logoUrl"]
        }
        data.append(temp_party)
    return jsonify({
        "status": 200,
        "data": data
    }), 200


@api.route('/parties', methods=['POST'])
def create_a_party():
    """Creates a party"""
    data = request.get_json()
    validation_response = validate_party_info(data)
    if validation_response is None:
        new_party = Party.create_party(
            data['id'], data['name'], data['hqAddress'], data['logoUrl'])
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
        return jsonify({"message": validation_response['message']}), validation_response['code']


@api.route('/parties/<int:party_id>', methods=['GET'])
def get_a_party(party_id):
    """Gets a specific party"""
    if not isinstance(party_id, int):
        return jsonify({"message": "id must be an integer"}), 400
    elif party_id < 0:
        return jsonify({"message": "Id can not be a negative"}), 400
    else:
        for party in parties:
            if party['id'] == party_id:
                return jsonify(party), 200
        return jsonify({"message": "party do not exists"}), 404


@api.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_a_party(party_id):
    """deletes a specific party"""
    if not isinstance(party_id, int):
        return jsonify({"message": "ID must be an integer"}), 400
    elif party_id < 0:
        return jsonify({"message": "ID must not be a negative integer"}), 400
    else:
        for party in parties:
            if party['id'] == party_id:
                party_index = parties.index(party)
                del(parties[party_index])
                return jsonify({
                    "status": 200,
                    "data": [
                        {
                            "message": "party deleted successfully"
                        }
                    ]
                }), 200
        return jsonify({
            "status": 404,
            "data": [{
                "message": "party does not exists"
            }]
        }), 404


@api.route('/parties/<int:party_id>/name', methods=['PATCH'])
def edit_a_party(party_id):
    """Edits a specific party"""
    data = request.get_json()
    if not data:
        return jsonify({"message": "You must provide data for editng a party"}), 400
    name = data.get("name", None)
    if not isinstance(party_id, int):
        return jsonify({"message": "ID must be an integer"}), 400
    elif name is None:
        return jsonify({'message': 'You must provide the new  name'}), 400
    elif len(data['name']) < 0:
        return jsonify({"message": "name cannot be empty"})
    else:
        for party in parties:
            if party['id'] == party_id:
                party['name'] = data['name']
                return jsonify({
                    "status": 200,
                    "data": [
                        {
                            "id": party['id'],
                            "name": party['name']
                        }
                    ]
                })
        return jsonify({"message": "Party does not exists"}), 404


@api.route('/offices', methods=['GET'])
def get_all_offices():
    """Gets all offices"""
    data = []
    for office in offices:
        temp_office = {
            "id": office["id"],
            "type": office["type"],
            "name": office["name"]
        }
        data.append(temp_office)
    return jsonify({
        "status": 200,
        "data": data
    }), 200


@api.route('/offices', methods=['POST'])
def create_an_office():
    """"creates a specific office"""
    data = request.get_json()
    if not data:
        return jsonify({"message": "You must provide data to create the office"}), 400
    office_id = data.get("id", None)
    office_type = data.get("type", None)
    office_name = data.get("name")
    if office_id is None:
        return jsonify({"message": "Id is required"}), 400
    elif office_type is None:
        return jsonify({"message": "Type required"}), 400
    elif office_name is None:
        return jsonify({"message": "Name is required"}), 400
    elif not isinstance(office_id, int):
        return jsonify({"message": "Office id must be an integer"}), 400
    elif not isinstance(office_name, str):
        return jsonify({"message": "Office name must be a string"}), 400
    elif find_item_by_id(office_id, offices):
        return jsonify({"message": "Office with that ID already exists"}), 400
    else:
        new_office = Office.create_office(office_id, office_type, office_name)
        return jsonify({
            "status": 201,
            "data": [{
                "id": new_office["id"],
                "type": new_office["type"],
                "name": new_office["name"]
            }]
        }), 201


@api.route('/offices/<int:office_id>', methods=['GET'])
def get_an_office(office_id):
    """Gets a specific office"""
    if not isinstance(office_id, int):
        return jsonify({
            "status": 400,
            "message": "the id must be an integer"
        }), 400
    elif office_id < 0:
        return jsonify({
            "status": 400,
            "message": "ID must be an positive integer"
        })
    else:
        for office in offices:
            if office["id"] == office_id:
                return jsonify({
                    "status": 200,
                    "data": [{
                        "id": office["id"],
                        "type": office["type"],
                        "name": office["name"]
                    }]
                }), 200
        return jsonify({
            "status": 404,
            "data": [{
                "message": "Office do not exists"
            }]
        }), 404


def bad_request(error):
    """defines custom  error handler for bad requests"""
    return jsonify({"message": "Something realy terrible happened......dont' wory!   it's NOT your fault ......MAYBE it is!"}), 400


def not_found_error(error):
    """Defines custom error handler for not found errors"""
    return jsonify({"message": "The url is not found on the server please check agian or make sure its typed correctly"}), 404
