from flask import jsonify
from flask_restful import Resource
from application.model.ApplicationUser import ApplicationUser
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from application.extensions import db


class AuthenticationService(Resource):
    @staticmethod
    def user_registration(username, email, password):
        # Check if the user already exists
        existing_user = ApplicationUser.query.filter_by(email=email).first()
        if existing_user:
            return jsonify(message="User already exists.")  # User already exists
        # Create a new user and add to the database
        new_user = ApplicationUser(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(
            message="user_successfully registered",
            data={
                "user_id": new_user.user_id,
                "username": new_user.username,
                "email": new_user.email,
                "role": new_user.role,
                "created_at": new_user.created_at.isoformat() if new_user.created_at else None,
            }), 201

    @staticmethod
    def user_login(email, password):
        existing_user = ApplicationUser.query.filter_by(email=email).first()
        if not existing_user or not existing_user.check_password(password):
            return jsonify(message="Incorrect email or password."), 401

        access_token = create_access_token(identity=str(existing_user.user_id))

        return jsonify(message="User successfully logged in.", access_token=access_token), 200

    @staticmethod
    @jwt_required()
    def get_all_users():
        user_identity = get_jwt_identity()
        print("Current user:", user_identity)
        print(ApplicationUser.query)
        users = ApplicationUser.query.all()
        return jsonify([{
             "user_id": user.user_id,
             "username": user.username,
             "email": user.email,
             "role": user.role
        } for user in users])
