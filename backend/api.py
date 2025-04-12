from flask_restful import Api, Resource
from flask import Flask, request, jsonify
from models import Product
from database import db

app = Flask(__name__)
api = Api(app)

# Recurso para manejar productos
class ProductResource(Resource):
    def get(self):
        products = Product.query.all()
        return jsonify([{
            "id": product.id,
            "code": product.code,
            "name": product.name,
            "cost_price": product.cost_price,
            "sale_price": product.sale_price,
            "stock": product.stock
        } for product in products])

class ProductDetailResource(Resource):
    def delete(self, product_id):
        product = Product.query.get(product_id)
        if not product:
            return jsonify({"error": "Producto no encontrado"}), 404

        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Producto eliminado exitosamente"})

# Registrar los recursos en la API
api.add_resource(ProductResource, '/api/products')
api.add_resource(ProductDetailResource, '/api/products/<int:product_id>')

if __name__ == '__main__':
    app.run(debug=True)