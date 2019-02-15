from flask import Blueprint, request
from flask import jsonify
from app.api.v2.utils import is_valid_email,  is_boolean, validate_name, validate_id
from app.api.v1.utils import ValidateUserInput, check_json
from app.api.v2.models.user_models import User
api2 = Blueprint("api2", __name__)


@api2.route('/parties')
def get_all_parties_2():
    return jsonify({'message': "things are realy good"})


@api2.route("/auth/signup", methods=['POST'])
def signup():
    user_input = request.get_json(force=True)
    data = check_json(user_input)
    if data:
        id = ValidateUserInput.check_id(user_input.get("id"))
        firstname = ValidateUserInput.check_string_types(
            user_input.get("firstname"))
        lastname = ValidateUserInput.check_string_types(
            user_input.get("lastname"))
        othername = ValidateUserInput.check_string_types(
            user_input.get("othername"))
        email = ValidateUserInput.check_string_types(
            user_input.get("email"))
        exists = User.user_exists(user_input.get("id"))
        password = ValidateUserInput.check_string_types(
            user_input.get("password"))
        phoneNumber = ValidateUserInput.check_string_types(
            user_input.get("phoneNumber"))
        passportUrl = ValidateUserInput.check_string_types(
            user_input.get("passportUrl"))
        isPolitician = ValidateUserInput.check_string_types(
            user_input.get("isPolitician"))
        isAdmin = ValidateUserInput.check_string_types(
            user_input.get("isAdmin"))

        if (id and firstname and lastname and othername and email and password and phoneNumber and isPolitician and isAdmin and passportUrl) and not exists:
            return jsonify({
                "status": 201,
                "data": [{
                }]
            }), 201
    return jsonify({
        "status": 400,
        "data": [{
            "message": "Check the data you are trying to send please"
        }]
    }), 400

    # user_input = request.get_json(force=True)
    # data = check_json(user_input)
    # validate_id(user_input.get("id"))
    # validate_name(user_input.get("firstname"))
    # validate_name(user_input.get("lastname"))
    # username = validate_name(user_input.get("username"))
    # email = is_valid_email(user_input.get("lastname"))
    # password = validate_name(user_input.get("password"))
    # othername = validate_name(user_input.get("othername"))
    # phone = validate_name(user_input.get("phoneNumber"))
    # passportUrl = validate_name(user_input.get(" passportUrl"))
    # isPolitician = is_boolean(user_input.get("isAdmin"))
    # isAdmin = is_boolean(user_input.get("isAdmin"))
    # user = User.user_exists(user_input.get("id"))
    # if user:
    #     return jsonify({"message": "user exists already"}), 400

    #     if (id and firstname and lastname and email and username and password and othername and isPolitician and phone and passportUrl and isAdmin):
    #         return jsonify({
    #             "status": 201,
    #             "data": [{
    #                 "message": "things look good"
    #             }]
    #         }), 201
    # return jsonify({
    #     "status": 400,
    #     "data": [{
    #         "message": "Check the data you are trying to send please"
    #     }]
    # }), 400
    # return jsonify({"message": "things are thick"})
