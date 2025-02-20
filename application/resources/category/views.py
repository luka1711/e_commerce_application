from flask import Blueprint, jsonify
from application.resources.category import category_service


category_bp = Blueprint('category',  __name__,  url_prefix='/category')


@category_bp.route('/')
def hello():
    return jsonify(message='Hello World!')