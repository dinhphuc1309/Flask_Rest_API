from flask import Blueprint, jsonify, request
from app.service.user_service import get_all_users, get_user_by_id, create_user

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify({'users': users})

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify({'user': user})
    else:
        return jsonify({'message': 'User not found'}), 404

@user_bp.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    user = create_user(data.get('username'), data.get('email'))
    return jsonify({'user': user}), 201
