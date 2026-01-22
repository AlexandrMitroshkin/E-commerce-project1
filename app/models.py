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
    

#в будуюзем возможно будет реализовано

# from datetime import datetime

# class Order(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
#     quantity = db.Column(db.Integer, default=1)
#     price = db.Column(db.Float)  # Цена на момент покупки
#     status = db.Column(db.String(50), default='processing')  # processing, shipped, delivered
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
#     # Связи
#     user = db.relationship('User', backref='orders')
#     product = db.relationship('Product')
    
#     def __repr__(self):
#         return f'<Order {self.id}>'
