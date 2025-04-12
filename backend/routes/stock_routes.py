from flask import Blueprint, jsonify
from models import Product
from flask import Blueprint, request, jsonify
from flask_socketio import emit
from models import db, Stock

stock_bp = Blueprint('stock', __name__)

@stock_bp.route('/low-stock', methods=['GET'])
def low_stock_alert():
    low_stock_products = Product.query.filter(Product.stock < 10).all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "stock": p.stock
    } for p in low_stock_products])

@stock_bp.route('/update-stock', methods=['POST'])
def update_stock():
    data = request.json
    stock_item = Stock.query.get(data['id'])
    
    if not stock_item:
        return jsonify({"error": "Artículo no encontrado"}), 404

    stock_item.quantity = data['quantity']
    db.session.commit()

    # Emitir un evento de notificación
    emit('stock_updated', {
        "id": stock_item.id,
        "name": stock_item.name,
        "quantity": stock_item.quantity
    }, broadcast=True)

    return jsonify({"message": "Stock actualizado"}), 200