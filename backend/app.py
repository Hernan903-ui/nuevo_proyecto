from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging
from database import init_database, db
from flask import jsonify, request
from models import Product
from utils.mail import init_mail
from flask_socketio import SocketIO


# Configuración de Flask
app = Flask(__name__)
init_database(app)
# Inicializar Flask-Mail
init_mail(app)
CORS(app)
# Inicializar Flask-SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

# Ejemplo de evento de conexión
@socketio.on('connect')
def handle_connect():
    print("Cliente conectado")

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/inventory_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{
        "id": product.id,
        "code": product.code,
        "name": product.name,
        "cost_price": product.cost_price,
        "sale_price": product.sale_price,
        "stock": product.stock
    } for product in products])

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Producto no encontrado"}), 404

    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Producto eliminado exitosamente"})

# Configuración de logs
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Importar rutas
from routes.auth_routes import auth_bp
from routes.product_routes import product_bp
from routes.stock_routes import stock_bp
from routes.report_routes import report_bp
from routes.pos_routes import pos_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(stock_bp, url_prefix='/stock')
app.register_blueprint(report_bp, url_prefix='/reports')
app.register_blueprint(pos_bp, url_prefix='/pos')

# Iniciar servidor
if __name__ == '__main__':
    socketio.run(app, debug=True)