from app import create_app, db
from app.models import Product, User
from datetime import datetime

app = create_app()

with app.app_context():
    print("Creating database tables...")
    db.create_all()
    
    print("Adding test products...")
    
    # Очищаем старые данные
    Product.query.delete()
    
    # Тестовые товары
    test_products = [
        # Мужская одежда
        {
            'name': 'T-shirt with Tape Details',
            'description': 'Comfortable cotton t-shirt with stylish tape details.',
            'price': 120.00,
            'category': 'men',
            'style': 'casual',
            'image': 'T-TAPE DETAILS.jpg',
            'rating': 4.5
        },
        {
            'name': 'Skinny Fit Jeans',
            'description': 'Modern skinny fit jeans made from premium denim.',
            'price': 240.00,
            'old_price': 260.00,
            'category': 'men',
            'style': 'casual',
            'image': 'SKINNY FIT JEANS.jpg',
            'rating': 3.5
        },
        {
            'name': 'Checkered Shirt',
            'description': 'Classic checkered shirt perfect for casual occasions.',
            'price': 180.00,
            'category': 'men',
            'style': 'casual',
            'image': 'CHECKERED SHIRT.jpg',
            'rating': 4.5
        },
        {
            'name': 'Sleeve Striped T-shirt',
            'description': 'Stylish striped t-shirt with unique sleeve design.',
            'price': 130.00,
            'old_price': 160.00,
            'category': 'men',
            'style': 'casual',
            'image': 'SLEEVE STRIPED.jpg',
            'rating': 4.5
        },
        
        # Женская одежда
        {
            'name': 'Gradient Graphic T-shirt',
            'description': 'Fashionable t-shirt with gradient graphic print.',
            'price': 145.00,
            'category': 'women',
            'style': 'casual',
            'image': 'Gradient Graphic T-shirt.jpg',
            'rating': 3.5
        },
        {
            'name': 'Polo with Tipping Details',
            'description': 'Elegant polo shirt with tipping details.',
            'price': 180.00,
            'category': 'women',
            'style': 'casual',
            'image': 'Polo with Tipping Details.jpg',
            'rating': 4.5
        },
        {
            'name': 'Black Striped T-shirt',
            'description': 'Classic black striped t-shirt.',
            'price': 120.00,
            'old_price': 150.00,
            'category': 'women',
            'style': 'casual',
            'image': 'Black Striped T-shirt.jpg',
            'rating': 5.0
        },
        {
            'name': 'Vertical Striped Shirt',
            'description': 'Fashionable vertical striped shirt.',
            'price': 212.00,
            'old_price': 232.00,
            'category': 'women',
            'style': 'casual',
            'image': 'VERTICAL STRIPED .jpg',
            'rating': 5.0
        },
        
        # Casual (унисекс)
        {
            'name': 'Courage Graphic T-shirt',
            'description': 'Graphic t-shirt with courage design.',
            'price': 145.00,
            'category': 'casual',
            'style': 'casual',
            'image': 'T-COURAGE GRAPHIC .jpg',
            'rating': 4.0
        },
        {
            'name': 'Loose Fit Bermuda Shorts',
            'description': 'Comfortable loose fit bermuda shorts.',
            'price': 80.00,
            'category': 'casual',
            'style': 'casual',
            'image': 'LOOSE FIT BERMUDA SHORTS.jpg',
            'rating': 3.0
        },
        {
            'name': 'Faded Skinny Jeans',
            'description': 'Fashionable faded skinny jeans.',
            'price': 210.00,
            'category': 'casual',
            'style': 'casual',
            'image': 'Faded Skinny Jeans.jpg',
            'rating': 4.5
        },
        {
            'name': 'Orange Color T-shirt',
            'description': 'Bright orange t-shirt.',
            'price': 95.00,
            'category': 'casual',
            'style': 'casual',
            'image': 'T-orange_color.jpg',
            'rating': 4.2
        },
        
        # Новинки
        {
            'name': 'One Life Graphic T-shirt',
            'description': 'New collection graphic t-shirt.',
            'price': 155.00,
            'category': 'novelty',
            'style': 'casual',
            'image': 'T-One Life Graphic.jpg',
            'rating': 4.8
        },
        {
            'name': 'Polo with Contrast Trims',
            'description': 'New polo with contrast trims.',
            'price': 190.00,
            'category': 'novelty',
            'style': 'casual',
            'image': 'Polo with Contrast Trims.jpg',
            'rating': 4.7
        }
    ]
    
    for prod_data in test_products:
        product = Product(
            name=prod_data['name'],
            description=prod_data['description'],
            price=prod_data['price'],
            old_price=prod_data.get('old_price'),
            category=prod_data['category'],
            style=prod_data['style'],
            image=prod_data['image'],
            rating=prod_data['rating']
        )
        db.session.add(product)
    
    db.session.commit()
    print(f"✅ Added {len(test_products)} test products to database!")