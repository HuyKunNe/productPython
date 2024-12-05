from flask import Flask
from flask_restful import Api
from controller.product_controller import ProductResource
from controller.product_controller import ProductResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ProductResource, '/products')

if __name__ == '__main__':
    app.run(debug=True)
