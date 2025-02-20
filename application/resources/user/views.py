from flask import Blueprint, jsonify, request
from application.resources.user.authentication_service import AuthenticationService

authentication_bp = Blueprint('authentication', __name__, url_prefix='/api/auth')


@authentication_bp.route('/register', methods=['POST'])
def user_registration():
    data = request.get_json()
    try:
        if not data:
            return jsonify({'message': 'No data'}), 400

        return AuthenticationService.user_registration(data['username'], data['email'], data['password'])
    except Exception as e:
        return jsonify({'exception': str(e), 'message': 'Wrong body provided. Required are username, email and password'}), 400


@authentication_bp.route('/login', methods=['POST'])
def user_login():
    data = request.get_json()
    try:
        if not data:
            return jsonify({'message': 'No data'}), 400
        else:
            return AuthenticationService.user_login(data['email'], data['password'])
    except:
        return jsonify({'message': 'Invalid body provided. Required are email and password'}), 400


@authentication_bp.route('/', methods=['GET'])
def get_users():
    return AuthenticationService.get_all_users()
