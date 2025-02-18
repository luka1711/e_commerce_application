# app/__init__.py
from flask import Flask
from application.extensions import db
from application.resources.user import user_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/e_commerce_data'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Initialize the database

    # Register the blueprints for different parts of the application
    app.register_blueprint(user_bp)

    with app.app_context():
        db.create_all()  # This will create all tables defined by your models

    return app
