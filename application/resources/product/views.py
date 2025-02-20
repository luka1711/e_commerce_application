from flask import Blueprint

from application.resources.product.product_service import ProductService


product_bp = Blueprint('product', __name__, url_prefix='/product')


@product_bp.route('/allProducts', methods=['GET'])
def get_products():
    return ProductService.get_products()
