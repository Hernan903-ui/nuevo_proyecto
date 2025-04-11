from flask import request, jsonify
from app import db
from models import Product, StockHistory, Sale

@app.route('/sales', methods=['POST'])
def register_sale():
    data = request.get_json()
    products = data.get('products', [])

    if not products:
        return jsonify({'error': 'No se proporcionaron productos para la venta'}), 400

    try:
        total_price = 0

        for item in products:
            product_id = item.get('product_id')
            quantity = item.get('quantity')
            sale_price = item.get('sale_price')

            # Verificar si el producto existe
            product = Product.query.get(product_id)
            if not product:
                return jsonify({'error': f'Producto con ID {product_id} no encontrado'}), 404

            # Verificar si hay suficiente stock
            if product.stock < quantity:
                return jsonify({'error': f'Stock insuficiente para el producto {product.name}'}), 400

            # Reducir el stock del producto
            product.stock -= quantity
            total_price += quantity * sale_price

            # Registrar la salida en el historial de stock
            stock_history = StockHistory(
                product_id=product_id,
                action='exit',
                quantity=quantity
            )
            db.session.add(stock_history)

            # Registrar la venta
            sale = Sale(
                product_id=product_id,
                quantity=quantity,
                sale_price=sale_price,
                total_price=quantity * sale_price
            )
            db.session.add(sale)

        # Confirmar los cambios en la base de datos
        db.session.commit()
        return jsonify({'message': 'Venta registrada exitosamente'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500