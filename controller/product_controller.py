# app/controllers/product_controller.py
from flask_restful import Resource, reqparse
from services.product_service import ProductService

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True,
                    help='Name of the product')
parser.add_argument('price', type=float, required=True,
                    help='Price of the product')


class ProductResource(Resource):
    def __init__(self):
        self.product_service = ProductService()

    def get(self):
        products = self.product_service.get_all_products()
        return [product.__dict__ for product in products]

    def post(self):
        data = parser.parse_args()
        product = self.product_service.create_product(
            data['name'], data['price'])
        return product.__dict__, 201
