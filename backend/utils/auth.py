from flask import request, jsonify
from functools import wraps
import jwt
from models import User

def role_required(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({"error": "Token no proporcionado"}), 401

            try:
                decoded = jwt.decode(token, 'your-secret-key', algorithms=['HS256'])
                user = User.query.get(decoded['id'])
                if not user or user.role != required_role:
                    return jsonify({"error": "Acceso no autorizado"}), 403
            except jwt.ExpiredSignatureError:
                return jsonify({"error": "Token expirado"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"error": "Token inválido"}), 401

            return func(*args, **kwargs)
        return wrapper
    return decorator