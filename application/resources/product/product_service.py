from flask_restful import Resource
from flask import jsonify
from application.extensions import db
from application.model.Product import Product


class ProductService(Resource):

    @staticmethod
    def get_products():
        products = Product.query.all()
        return jsonify(data=products), 200
