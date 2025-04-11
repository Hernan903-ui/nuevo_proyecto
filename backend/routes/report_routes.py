from flask import Blueprint, jsonify, send_file
from models import Product, StockHistory
from utils.pdf_generator import generate_pdf
from database import db_session
from sqlalchemy.sql import text

report_bp = Blueprint('reports', __name__)

@report_bp.route('/sales-analysis', methods=['GET'])
def sales_analysis():
    products = Product.query.all()
    analysis = {
        "most_sold": max(products, key=lambda p: p.stock),
        "least_sold": min(products, key=lambda p: p.stock)
    }
    return jsonify(analysis)

@report_bp.route('/generate-pdf', methods=['GET'])
def generate_report_pdf():
    stock_history = StockHistory.query.all()
    data = [{"product_id": sh.product_id, "action": sh.action, "quantity": sh.quantity, "date": sh.date} for sh in stock_history]
    filename = "stock_report.pdf"
    generate_pdf(data, filename)
    return send_file(filename, as_attachment=True)

# Ruta para obtener los productos más vendidos
@report_bp.route('/reports/most-sold', methods=['GET'])
def most_sold_products():
    try:
        query = text("""
            SELECT 
                p.name AS product_name, 
                SUM(s.quantity) AS total_sold
            FROM 
                sales s
            INNER JOIN 
                products p ON s.product_id = p.id
            GROUP BY 
                p.name
            ORDER BY 
                total_sold DESC
            LIMIT 10
        """)
        result = db_session.execute(query).fetchall()

        most_sold = [{"product_name": row["product_name"], "total_sold": row["total_sold"]} for row in result]
        return jsonify(most_sold), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ruta para obtener los productos más rentables
@report_bp.route('/reports/most-profitable', methods=['GET'])
def most_profitable_products():
    try:
        query = text("""
            SELECT 
                p.name AS product_name, 
                SUM((s.sale_price - s.cost_price) * s.quantity) AS total_profit
            FROM 
                sales s
            INNER JOIN 
                products p ON s.product_id = p.id
            GROUP BY 
                p.name
            ORDER BY 
                total_profit DESC
            LIMIT 10
        """)
        result = db_session.execute(query).fetchall()

        most_profitable = [{"product_name": row["product_name"], "total_profit": row["total_profit"]} for row in result]
        return jsonify(most_profitable), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500