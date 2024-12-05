# app/services/product_service.py
from repository.product_repository import ProductRepository
from models.product_model import Product


class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def create_product(self, name, price):
        product = Product(
            id=len(self.product_repository.products) + 1, name=name, price=price)
        return self.product_repository.add_product(product)

    def get_all_products(self):
        return self.product_repository.get_all_products()

    def get_product_by_id(self, product_id):
        return self.product_repository.get_product_by_id(product_id)

    def update_product(self, product_id, name, price):
        return self.product_repository.update_product(product_id, name, price)

    def delete_product(self, product_id):
        return self.product_repository.delete_product(product_id)
