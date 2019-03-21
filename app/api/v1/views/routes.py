from flask import jsonify, request
from flask import Blueprint
"""Module for handling requests and request routings"""
from app.api.v1.models.party_models import Party, parties
from app.api.v1.models.office_models import Office, offices
from app.api.v1.utils import check_json, ValidateUserInput

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
    user_input = request.get_json(force=True)
    data = check_json(user_input)
    if data:
        id = ValidateUserInput.check_id(user_input.get("id"))
        name = ValidateUserInput.check_string_types(user_input.get("name"))
        hqAddress = ValidateUserInput.check_string_types(
            user_input.get("hqAddress"))
        logoUrl = ValidateUserInput.check_string_types(
            user_input.get("logoUrl"))
        exists = ValidateUserInput.item_exists(user_input.get("id"), parties)
        if ((id and name and hqAddress)and(logoUrl)) and not exists:
            new_party = Party.create_party(user_input.get("id"), user_input.get(
                "name"), user_input.get("hqAddress"), user_input.get("logoUrl"))
            return jsonify({
                "status": 201,
                "data": [{
                    "id": new_party["id"],
                    "name": new_party["name"]
                }]
            }), 201
    return jsonify({
        "status": 400,
        "data": [{
            "message": "Check the data you are trying to send please"
        }]
    }), 400


@api.route('/parties/<int:party_id>', methods=['GET'])
def get_a_party(party_id):
    id_is_valid = ValidateUserInput.check_id(party_id)
    if id_is_valid:
        party = ValidateUserInput.find_by_id(party_id, parties)
        if party is not None:
            return jsonify({
                "status": 200,
                "data": [{
                    "id": party["id"],
                    "name": party["name"],
                    "logoUrl": party["logoUrl"]
                }]
            }), 200
    return jsonify({
        "status": 404,
        "data": [{
            "message": "Please check the data you are trying to send!"
        }]
    }), 404


@api.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_a_party(party_id):
    """deletes a specific party"""
    id_is_valid = ValidateUserInput.check_id(party_id)
    if id_is_valid:
        party = ValidateUserInput.find_by_id(party_id, parties)
        if party is not None:
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
    user_input = request.get_json(force=True)
    data = check_json(user_input)
    if data:
        name = ValidateUserInput.check_string_types(user_input.get("name"))
        if name:
            party_to_edit = ValidateUserInput.find_by_id(party_id, parties)
            if party_to_edit is not None:
                party_to_edit['name'] = user_input['name']
                return jsonify({
                    "status": 200,
                    "data": [
                        {
                            "id": party_to_edit['id'],
                            "name": party_to_edit['name']
                        }
                    ]
                }), 200
    return jsonify({
        "status": 400,
        "data": [{
            "message": "Please check the data you are trying to submit"
        }]
    }), 400


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
    """Creates an office"""
    user_input = request.get_json(force=True)
    data = check_json(user_input)
    if data:
        id = ValidateUserInput.check_id(user_input.get("id"))
        name = ValidateUserInput.check_string_types(user_input.get("name"))
        type = ValidateUserInput.check_string_types(
            user_input.get("type"))
        exists = ValidateUserInput.item_exists(user_input.get("id"), offices)
        if (id and name and type)and not exists:
            new_office = Office.create_office(user_input.get("id"), user_input.get(
                "type"), user_input.get("name"))
            return jsonify({
                "status": 201,
                "data": [{
                    "id": new_office["id"],
                    "name": new_office["name"]
                }]
            }), 201
    return jsonify({
        "status": 400,
        "data": [{
            "message": "Check the data you are trying to send please"
        }]
    }), 400


@api.route('/offices/<int:office_id>', methods=['GET'])
def get_an_office(office_id):
    """Gets a specific office"""
    id_is_valid = ValidateUserInput.check_id(office_id)
    if id_is_valid:
        office = ValidateUserInput.find_by_id(office_id, offices)
        if office is not None:
            return jsonify({
                "status": 200,
                "data": [{
                    "id": office["id"],
                    "name": office["name"]
                }]
            }), 200
    return jsonify({
        "status": 400,
        "data": [{
            "message": "Please try and check the data you are trying to send "
        }]
    }), 400


@api.route('/', methods=['GET'])
def home():
    return(jsonify({
        "status": 200,
        "data": [{
            "message": "Welcome to politica API, Remeber This is An API"
        }]
    }))


def bad_request(error):
    """defines custom  error handler for bad requests"""
    return jsonify({"message": "Something realy terrible happened......dont' wory!   it's NOT your fault ......MAYBE it is!"}), 400


def not_found_error(error):
    """Defines custom error handler for not found errors"""
    return jsonify({"message": "The url is not found on the server please check agian or make sure its typed correctly"}), 404
