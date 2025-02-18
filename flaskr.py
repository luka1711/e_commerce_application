from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.extensions import db
from flask import Blueprint, jsonify
from application.routes import bp


from application import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)