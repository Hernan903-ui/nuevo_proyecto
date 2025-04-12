from flask import Blueprint, jsonify

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/api/dashboard-data', methods=['GET'])
def get_dashboard_data():
    data = {
        "totalSales": [5000, 7000, 8000, 12000, 15000],  # Datos de ejemplo
        "bestSellers": [
            {"name": "Producto A", "y": 40},
            {"name": "Producto B", "y": 30},
            {"name": "Producto C", "y": 20},
            {"name": "Producto D", "y": 10}
        ]
    }
    return jsonify(data)