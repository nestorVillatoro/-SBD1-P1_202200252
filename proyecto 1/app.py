from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Cambiar a Oracle si es necesario
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'supersecretkey'  # Clave para JWT

db = SQLAlchemy(app)
jwt = JWTManager(app)

@app.route('/')
def home():
    return jsonify({"message": "Bienvenido a la API del Sistema de Ventas"}), 200


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15))


with app.app_context():
    db.create_all()
    
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


@app.route('/api/users/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({"message": "Credenciales inválidas"}), 401
    
    access_token = create_access_token(identity=user.id)
    return jsonify({"status": "success", "token": access_token}), 200


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default="processing")
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = db.relationship('User', backref=db.backref('orders', lazy=True))


@app.route('/api/orders', methods=['POST'])
@jwt_required()
def create_order():
    data = request.get_json()
    
    user_id = data.get('user_id')
    total_amount = data.get('total_amount')
    
    if not user_id or not total_amount:
        return jsonify({"message": "Datos incompletos"}), 400
    
    new_order = Order(user_id=user_id, total_amount=total_amount)
    db.session.add(new_order)
    db.session.commit()
    
    return jsonify({
        "status": "success",
        "message": "Orden creada exitosamente",
        "order_id": new_order.id
    }), 201


@app.route('/api/orders', methods=['GET'])
@jwt_required()
def list_orders():
    orders = Order.query.all()
    return jsonify({"orders": [
        {"id": order.id, "user_id": order.user_id, "total_amount": order.total_amount, "status": order.status}
        for order in orders
    ]}), 200


@app.route('/api/orders/<int:id>', methods=['PUT'])
@jwt_required()
def update_order(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({"message": "Orden no encontrada"}), 404
    
    data = request.get_json()
    order.status = data.get("status", order.status)
    db.session.commit()
    
    return jsonify({"status": "success", "message": "Orden actualizada exitosamente"}), 200


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    method = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default="pending")
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    order = db.relationship('Order', backref=db.backref('payments', lazy=True))


@app.route('/api/payments', methods=['POST'])
@jwt_required()
def register_payment():
    data = request.get_json()
    
    order_id = data.get('order_id')
    amount = data.get('amount')
    method = data.get('method')
    
    if not order_id or not amount or not method:
        return jsonify({"message": "Datos incompletos"}), 400
    
    new_payment = Payment(order_id=order_id, amount=amount, method=method, status="approved")
    db.session.add(new_payment)
    db.session.commit()
    
    return jsonify({
        "status": "success",
        "message": "Pago registrado exitosamente",
        "payment_id": new_payment.id
    }), 201


@app.route('/api/payments', methods=['GET'])
@jwt_required()
def list_payments():
    payments = Payment.query.all()
    return jsonify({"payments": [
        {"id": payment.id, "order_id": payment.order_id, "amount": payment.amount, "method": payment.method, "status": payment.status}
        for payment in payments
    ]}), 200


@app.route('/api/users/<int:id>', methods=['GET'])
@jwt_required()
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"message": "Usuario no encontrado"}), 404
    
    return jsonify({"id": user.id, "username": user.username, "email": user.email, "phone": user.phone}), 200

if __name__ == '__main__':
    app.run(debug=True)
