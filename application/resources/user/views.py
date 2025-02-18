from flask import Blueprint, jsonify, request
from application.resources.user.user_service import UserService
from application.model import ApplicationUser

user_bp = Blueprint('user_', __name__, url_prefix='/api/users')


@user_bp.route('/register', methods=['POST'])
def user_registration():
    data = request.get_json()
    try:
        if not data:
            return jsonify({'message': 'No data'}), 400

        return UserService.user_registration(data['username'], data['email'], data['password'])
    except Exception as e:
        return jsonify({'exception': str(e), 'message': 'Wrong body provided. Required are username, email and password'}), 400


@user_bp.route('/login', methods=['POST'])
def user_login():
    data = request.get_json()
    try:
        if not data:
            return jsonify({'message': 'No data'}), 400
        else:
            return UserService.user_login(data['email'], data['password'])
    except:
        return jsonify({'message': 'Invalid body provided. Required are email and password'}), 400


@user_bp.route('/', methods=['GET'])
def get_users():
    return UserService.get_all_users()
