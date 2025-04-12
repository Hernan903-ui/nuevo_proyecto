from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Campo para la contraseña
    email = db.Column(db.String(100), unique=True, nullable=False)
    business_name = db.Column(db.String(100), unique=True, nullable=False)
    registered_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    role = db.Column(db.String(50), nullable=False, default='user')  # Nuevo campo para roles

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    cost_price = db.Column(db.Float, nullable=False)
    sale_price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    last_updated = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'))

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(200))

class StockHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    action = db.Column(db.String(50), nullable=False)  # 'entry' o 'exit'
    quantity = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relación para acceder al producto desde el historial
    product = db.relationship('Product', backref=db.backref('stock_history', lazy=True))

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)  # Relación con la tabla Product
    quantity = db.Column(db.Integer, nullable=False)  # Cantidad de producto vendido
    sale_price = db.Column(db.Float, nullable=False)  # Precio de venta por unidad
    total_price = db.Column(db.Float, nullable=False)  # Precio total (cantidad * precio unitario)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())  # Fecha de la venta
    customer_name = db.Column(db.String(100))  # Opcional: Nombre del cliente (si se requiere)

    # Relación para acceder al producto desde la venta
    product = db.relationship('Product', backref=db.backref('sales', lazy=True))