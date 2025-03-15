from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Inicializar Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Cambiar a Oracle si es necesario
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'supersecretkey'  # Clave para JWT

db = SQLAlchemy(app)
jwt = JWTManager(app)

@app.route('/')
def home():
    return jsonify({"message": "Bienvenido a la API del Sistema de Ventas"}), 200

# Modelos
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15))

# CREAR BASE DE DATOS AL EJECUTAR
with app.app_context():
    db.create_all()
    

# Registro de usuario
@app.route('/api/users', methods=['POST'])
def register_user():
    data = request.get_json()
    if not data or not all(k in data for k in ("username", "email", "password", "phone")):
        return jsonify({"message": "Datos incompletos"}), 400
    
    if User.query.filter_by(username=data['username']).first() or User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "El usuario o email ya existe"}), 409
    
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password, phone=data['phone'])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"status": "success", "message": "Usuario creado exitosamente"}), 201

# Login de usuario
@app.route('/api/users/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({"message": "Credenciales inválidas"}), 401
    
    access_token = create_access_token(identity=user.id)
    return jsonify({"status": "success", "token": access_token}), 200

# Obtener perfil de usuario
@app.route('/api/users/<int:id>', methods=['GET'])
@jwt_required()
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"message": "Usuario no encontrado"}), 404
    
    return jsonify({"id": user.id, "username": user.username, "email": user.email, "phone": user.phone}), 200

if __name__ == '__main__':
    app.run(debug=True)
