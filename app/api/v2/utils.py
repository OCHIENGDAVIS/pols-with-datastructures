from flask import jsonify, make_response


def validate_id(id):
    if not isinstance(id, int):
        return jsonify({"message": "invalid input"}), 400


def is_boolean(is_admin):
    if not isinstance(is_admin, bool):
        return jsonify({"message": "invalid input"}), 400


def is_valid_email(email):
    if email and (not "@" in email):
        return jsonify({'message': 'invalid input'}), 400
    return True


def validate_name(name):
    if isinstance(name, str) or name == "":
        return jsonify({'message': "invalid input"}), 400
    return True
