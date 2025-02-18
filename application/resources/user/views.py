from flask import Blueprint, jsonify, request
from application.resources.user.user_service import UserService
from application.model import ApplicationUser

user_bp = Blueprint('user_', __name__, url_prefix='/api/users')


@user_bp.route('/', methods=['POST'])
def user_registration():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data'}), 400

    return UserService.user_registration(data['username'], data['email'], data['password'])


@user_bp.route('/', methods=['GET'])
def get_users():
    return UserService.get_all_users()