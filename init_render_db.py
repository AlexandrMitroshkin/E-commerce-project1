print("=" * 60)
print("🚀 RAILWAY DATABASE INITIALIZATION")
print("=" * 60)

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

try:
    from app import create_app, db
    from app.models import Product, User
    print("✅ Modules imported successfully")
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)

def main():
    try:
        app = create_app()
        
        with app.app_context():
            print("📦 Creating tables...")
            print(f"📁 Database path: {app.config['SQLALCHEMY_DATABASE_URI']}")

            db_path = '/tmp/shop.db'
            if os.path.exists(db_path):
                print("🗑️  Removing old database...")
                os.remove(db_path)
    
            db.create_all()
            print("✅ Tables created successfully!")

            print("📥 Adding test products...")

            test_products = [
                # Мужская одежда
                {
                    'name': 'T-shirt with Tape Details',
                    'description': 'Comfortable cotton t-shirt with stylish tape details.',
                    'price': 120.00,
                    'category': 'men',
                    'status':'bests',
                    'image': 'T-TAPE DETAILS.jpg',
                    'rating': 4.5
                },
                {
                    'name': 'Skinny Fit Jeans',
                    'description': 'Modern skinny fit jeans made from premium denim.',
                    'price': 240.00,
                    'old_price': 260.00,
                    'category': 'men',
                    'status':'bests',
                    'image': 'SKINNY FIT JEANS.jpg',
                    'rating': 4.5
                },
                {
                    'name': 'Long sleeved T-shirt',
                    'description': 'Comfortable cotton Long sleeved T-shirt.',
                    'price': 150.00,
                    'category': 'men',
                    'status':'bests',
                    'image': 'long sleeved T-shirt.jpg',
                    'rating': 5.0
                },
                {
                    'name': 'Teyes Team T-shirt',
                    'description': 'Comfortable cotton T-shirt.',
                    'price': 170.00,
                    'category': 'men',
                    'status':'bests',
                    'image': 'Teyes Team T-shirt.jpg',
                    'rating': 4.5
                },
                {
                    'name': 'Tom tailor T-shirt',
                    'description': 'Comfortable cotton t-shirt.',
                    'price': 180.00,
                    'category': 'men',
                    'status':'bests',
                    'image': 'Tom tailor T-shirt.jpg',
                    'rating': 5.0
                },
                {
                    'name': 'Zara shirt',
                    'description': 'Comfortable cotton Zara shirt.',
                    'price': 200.00,
                    'category': 'men',
                    'status':'bests',
                    'image': 'Zara shirt.jpg',
                    'rating': 5.0
                },
                
                # Женская одежда
                {
                    'name': 'Gradient Graphic T-shirt',
                    'description': 'Fashionable t-shirt with gradient graphic print.',
                    'price': 145.00,
                    'category': 'women',
                    'status':'bests',
                    'image': 'Gradient Graphic T-shirt.jpg',
                    'rating': 3.5
                },
                {
                    'name': 'Polo with Tipping Details',
                    'description': 'Elegant polo shirt with tipping details.',
                    'price': 180.00,
                    'category': 'women',
                    'status':'bests',
                    'image': 'Polo with Tipping Details.jpg',
                    'rating': 4.5
                },
                {
                    'name': 'Black Striped T-shirt',
                    'description': 'Classic black striped t-shirt.',
                    'price': 120.00,
                    'old_price': 150.00,
                    'category': 'women',
                    'status':'bests',
                    'image': 'Black Striped T-shirt.jpg',
                    'rating': 5.0
                },
                {
                    'name': 'Vertical Striped Shirt',
                    'description': 'Fashionable vertical striped shirt.',
                    'price': 212.00,
                    'old_price': 232.00,
                    'category': 'women',
                    'status':'bests',
                    'image': 'VERTICAL STRIPED .jpg',
                    'rating': 5.0
                },
                {
                    'name': 'Pink shirt',
                    'description': 'Comfortable cotton shirt.',
                    'price': 145.00,
                    'category': 'women',
                    'status':'bests',
                    'image': 'pink shirt.jpg',
                    'rating': 4.5
                },
                {
                    'name': 'Pink cap',
                    'description': 'Comfortable cotton cap.',
                    'price': 50.00,
                    'category': 'women',
                    'status':'bests',
                    'image': 'pink cap.jpg',
                    'rating': 4.5
                },
                
                # Casual
                {
                    'name': 'Courage Graphic T-shirt',
                    'description': 'Graphic t-shirt with courage design.',
                    'price': 145.00,
                    'category': 'casual',
                    'status':'.',
                    'image': 'T-COURAGE GRAPHIC .jpg',
                    'rating': 4.0
                },
                {
                    'name': 'Loose Fit Bermuda Shorts',
                    'description': 'Comfortable loose fit bermuda shorts.',
                    'price': 80.00,
                    'category': 'casual',
                    'status':'.',
                    'image': 'LOOSE FIT BERMUDA SHORTS.jpg',
                    'rating': 3.0
                },
                {
                    'name': 'Faded Skinny Jeans',
                    'description': 'Fashionable faded skinny jeans.',
                    'price': 210.00,
                    'category': 'casual',
                    'status':'.',
                    'image': 'Faded Skinny Jeans.jpg',
                    'rating': 4.5
                },
                {
                    'name': 'Orange Color T-shirt',
                    'description': 'Bright orange t-shirt.',
                    'price': 95.00,
                    'category': 'casual',
                    'status':'.',
                    'image': 'T-orange_color.jpg',
                    'rating': 4.2
                },
                {
                    'name': 'Tommy Helfiger T-shirt',
                    'description': 'Original Tommy Helfiger T-shirt',
                    'price': 195.00,
                    'category': 'casual',
                    'status':'.',
                    'image': 'Tom tailor T-shirt.jpg',
                    'rating': 4.5
                },
                {
                    'name': 'Balensiaga jacket',
                    'description': 'balensiaga jacket.jpg',
                    'price': 295.00,
                    'category': 'casual',
                    'status':'.',
                    'image': 'balensiaga jacket.jpg',
                    'rating': 5.0
                },
                
                # Новинки
                {
                    'name': 'One Life Graphic T-shirt',
                    'description': 'New collection graphic t-shirt.',
                    'price': 155.00,
                    'category': 'novelty',
                    'status':'.',
                    'image': 'T-One Life Graphic (2).jpg',
                    'rating': 4.8
                },
                {
                    'name': 'Polo with Contrast Trims',
                    'description': 'New polo with contrast trims.',
                    'price': 190.00,
                    'category': 'novelty',
                    'status':'.',
                    'image': 'Polo with Contrast Trims.jpg',
                    'rating': 4.7
                },
                {
                    'name': 'Checkered Shirt',
                    'description': 'Classic checkered shirt perfect for casual occasions.',
                    'price': 180.00,
                    'category': 'novelty',
                    'status':'.',
                    'image': 'CHECKERED SHIRT.jpg',
                    'rating': 4.5
                },
                {
                    'name': 'Sleeve Striped T-shirt',
                    'description': 'Stylish striped t-shirt with unique sleeve design.',
                    'price': 130.00,
                    'old_price': 160.00,
                    'category': 'novelty',
                    'status':'.',
                    'image': 'SLEEVE STRIPED.jpg',
                    'rating': 4.5
                },
                #Спорт
                {
                    'name': 'Black sport T-shirt',
                    'description': 'Black sport T-shirt for sportsmens',
                    'price': 130.00,
                    'old_price': 160.00,
                    'category': 'gym',
                    'status':'.',
                    'image': 'Black sport T-shirt.jpg',
                    'rating': 4.5
                },
                {
                    'name': 'Grey sport T-shirt',
                    'description': 'Grey sport T-shirt for sportsmens',
                    'price': 130.00,
                    'old_price': 160.00,
                    'category': 'gym',
                    'status':'.',
                    'image': 'Grey sport T-shirt.jpg',
                    'rating': 4.5
                },
                {
                    'name': 'White sport T-shirt',
                    'description': 'White sport T-shirt for sportsmens',
                    'price': 150.00,
                    'old_price': 170.00,
                    'category': 'gym',
                    'status':'.',
                    'image': 'White sport T-shirt.jpg',
                    'rating': 5.0
                },
                {
                    'name': 'Puma Jacket',
                    'description': 'Sport Jacket for sportsmens',
                    'price': 150.00,
                    'old_price': 170.00,
                    'category': 'gym',
                    'status':'.',
                    'image': 'puma jacket.jpg',
                    'rating': 4.0
                },
                {
                    'name': 'Sportive long sleeved T-shirt',
                    'description': 'Sportive long sleeved for sportsmens',
                    'price': 160.00,
                    'old_price': 180.00,
                    'category': 'gym',
                    'status':'.',
                    'image': 'sportive long sleeved T-shirt.jpg',
                    'rating': 4.0
                },
                {
                    'name': 'Stussy T-shirt',
                    'description': 'Original Stussy T-shirt',
                    'price': 170.00,
                    'old_price': 180.00,
                    'category': 'gym',
                    'status':'.',
                    'image': 'stussy T-shirt.jpg',
                    'rating': 3.5
                }     
            ]
            
            for prod_data in test_products:
                product = Product(
                    name=prod_data['name'],
                    description=prod_data['description'],
                    price=prod_data['price'],
                    old_price=prod_data.get('old_price'),
                    category=prod_data['category'],
                    status=prod_data['status'],
                    image=prod_data['image'],
                    rating=prod_data['rating']
                )
                db.session.add(product)
            
            db.session.commit()
            print(f"✅ Added {len(test_products)} products!")

            product_count = Product.query.count()
            print(f"📊 Total products in database: {product_count}")

            if os.path.exists('/tmp/shop.db'):
                size = os.path.getsize('/tmp/shop.db')
                print(f"📄 Database file exists: {size} bytes")
            else:
                print("⚠️  Database file not found!")
                
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

    print("=" * 60)
    print("✅ RAILWAY DATABASE INITIALIZATION COMPLETED")
    print("=" * 60)

if __name__ == "__main__":
    main()