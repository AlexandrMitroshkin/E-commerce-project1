from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer, default=0)
    category = db.Column(db.String(50))
    image = db.Column(db.String(100))
    description = db.Column(db.Text)
    
    @property
    def discount_price(self):
        return self.price * (1 - self.discount / 100)

    def __repr__(self):
        return f'<Product {self.name}>'