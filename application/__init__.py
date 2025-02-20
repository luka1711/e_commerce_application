# app/__init__.py
from flask import Flask
from application.extensions import db, jwt
from application.config import Config
from application.resources.user import authentication_bp
from application.resources.product import product_bp
from application.resources.category import category_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/e_commerce_data'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(Config)

    db.init_app(app)  # Initialize the database
    jwt.init_app(app)

    # Register the blueprints for different parts of the application
    app.register_blueprint(authentication_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(category_bp)

    with app.app_context():
        db.create_all()  # This will create all tables defined by your models

    return app
