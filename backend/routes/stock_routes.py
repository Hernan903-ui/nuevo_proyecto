from flask import Blueprint, jsonify
from models import Product

stock_bp = Blueprint('stock', __name__)

@stock_bp.route('/low-stock', methods=['GET'])
def low_stock_alert():
    low_stock_products = Product.query.filter(Product.stock < 10).all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "stock": p.stock
    } for p in low_stock_products])