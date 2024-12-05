# app/repositories/product_repository.py
from models.product_model import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        return product

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, product_id):
        return next((p for p in self.products if p.id == product_id), None)

    def update_product(self, product_id, name, price):
        product = self.get_product_by_id(product_id)
        if product:
            product.name = name
            product.price = price
            return product
        return None

    def delete_product(self, product_id):
        product = self.get_product_by_id(product_id)
        if product:
            self.products.remove(product)
            return product
        return None
