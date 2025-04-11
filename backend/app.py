from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging
from database import init_database, db

# Configuración de Flask
app = Flask(__name__)
init_database(app)
CORS(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/inventory_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configuración de logs
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Importar rutas
from routes.auth_routes import auth_bp
from routes.product_routes import product_bp
from routes.stock_routes import stock_bp
from routes.report_routes import report_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(stock_bp, url_prefix='/stock')
app.register_blueprint(report_bp, url_prefix='/stock')

# Iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)