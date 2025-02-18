from flask import jsonify, current_app
from flask_restful import Resource
from application.model.ApplicationUser import ApplicationUser
from application.extensions import db


class UserService(Resource):
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
        }), 201  # Return the newly created user

    @staticmethod
    def get_all_users():
        with current_app.app_context():  # Ensures the app context is available
            print(ApplicationUser.query)
            users = ApplicationUser.query.all()
            return jsonify([{
                "user_id": user.user_id,
                "username": user.username,
                "email": user.email,
                "role": user.role
            } for user in users])