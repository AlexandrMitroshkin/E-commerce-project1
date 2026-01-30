from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# ===== МОДЕЛЬ ПОЛЬЗОВАТЕЛЯ =====
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'

# ===== МОДЕЛЬ ТОВАРА =====
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    old_price = db.Column(db.Float)  # для скидки
    category = db.Column(db.String(50))  # 'men', 'women', 'casual', 'novelty', 'sales', 'unisex'
    style = db.Column(db.String(50))  # 'casual', 'formal', 'party', 'gym'
    image = db.Column(db.String(200))  # имя файла в папке static/img/
    rating = db.Column(db.Float, default=4.5)  # рейтинг 1-5
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Product {self.name}>'