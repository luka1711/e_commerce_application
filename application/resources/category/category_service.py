from flask_restful import Resource

from application.model.Category import Category


class CategoryService(Resource):
    @staticmethod
    def get_all():
        categories = Category.query.all()