from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from utils.mail import mail
from utils.auth import role_required
import jwt
from datetime import datetime
from datetime import timedelta

auth_bp = Blueprint('auth', __name__)

# Configuración del serializador para generar tokens
s = URLSafeTimedSerializer('your-secret-key')

# Ruta para solicitar un restablecimiento de contraseña
@auth_bp.route('/request-reset', methods=['POST'])
def request_password_reset():
    data = request.json
    email = data.get('email')

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    # Generar un token único
    token = s.dumps(email, salt='password-reset-salt')

    # Crear un mensaje de correo
    msg = Message('Restablecimiento de Contraseña',
                  sender='tu_correo@example.com',
                  recipients=[email])
    reset_url = f"http://localhost:5000/reset-password?token={token}"
    msg.body = f"Hola, haz clic en el siguiente enlace para restablecer tu contraseña: {reset_url}"
    mail.send(msg)

    return jsonify({"message": "Correo de restablecimiento enviado"}), 200

# Ruta para restablecer la contraseña
@auth_bp.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.json
    token = data.get('token')
    new_password = data.get('new_password')

    try:
        email = s.loads(token, salt='password-reset-salt', max_age=3600)  # Token válido por 1 hora
    except Exception as e:
        return jsonify({"error": "Token inválido o caducado"}), 400

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    # Actualizar la contraseña
    user.password = generate_password_hash(new_password, method='sha256')
    db.session.commit()

    return jsonify({"message": "Contraseña actualizada exitosamente"}), 200

@auth_bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='sha256')
    try:
        new_user = User(
            name=data['name'],
            email=data['email'],
            business_name=data['business_name'],
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Usuario registrado con éxito"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@auth_bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        token = jwt.encode({
            'id': user.id,
            'role': user.role,  # Incluye el rol en el token
            'exp': datetime.utcnow() + timedelta(hours=24)
        }, 'your-secret-key', algorithm='HS256')
        return jsonify({'token': token}), 200
    return jsonify({"error": "Credenciales inválidas"}), 401

@auth_bp.route('/admin-only', methods=['GET'])
@role_required('admin')  # Solo los administradores pueden acceder a esta ruta
def admin_only():
    return jsonify({"message": "Bienvenido, administrador"})