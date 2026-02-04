from app import create_app, db
from app.models import Product, User
import os

app = create_app()

def populate_initial_data():
    """Заполняет базу данных ВСЕМИ 36 товарами"""
    with app.app_context():

        existing_count = Product.query.count()
        print(f"📊 Existing products in DB: {existing_count}")
        
        if existing_count >= 36: 
            print("✅ Database already has full data, skipping population")
            return
        
        print("📥 Populating database with ALL 36 products...")

        all_products = [
            # Мужская одежда (6 товаров)
            {
                'name': 'T-shirt with Tape Details',
                'description': 'Comfortable cotton t-shirt with stylish tape details.',
                'price': 120.00,
                'category': 'men',
                'status': 'bests',
                'image': 'T-TAPE DETAILS.jpg',
                'rating': 4.5
            },
            {
                'name': 'Skinny Fit Jeans',
                'description': 'Modern skinny fit jeans made from premium denim.',
                'price': 240.00,
                'old_price': 260.00,
                'category': 'men',
                'status': 'bests',
                'image': 'SKINNY FIT JEANS.jpg',
                'rating': 4.5
            },
            {
                'name': 'Long sleeved T-shirt',
                'description': 'Comfortable cotton Long sleeved T-shirt.',
                'price': 150.00,
                'category': 'men',
                'status': 'bests',
                'image': 'long sleeved T-shirt.jpg',
                'rating': 5.0
            },
            {
                'name': 'Teyes Team T-shirt',
                'description': 'Comfortable cotton T-shirt.',
                'price': 170.00,
                'category': 'men',
                'status': 'bests',
                'image': 'Teyes Team T-shirt.jpg',
                'rating': 4.5
            },
            {
                'name': 'Tom tailor T-shirt',
                'description': 'Comfortable cotton t-shirt.',
                'price': 180.00,
                'category': 'men',
                'status': 'bests',
                'image': 'Tom tailor T-shirt.jpg',
                'rating': 5.0
            },
            {
                'name': 'Zara shirt',
                'description': 'Comfortable cotton Zara shirt.',
                'price': 200.00,
                'category': 'men',
                'status': 'bests',
                'image': 'Zara shirt.jpg',
                'rating': 5.0
            },
            
            # Женская одежда (6 товаров)
            {
                'name': 'Gradient Graphic T-shirt',
                'description': 'Fashionable t-shirt with gradient graphic print.',
                'price': 145.00,
                'category': 'women',
                'status': 'bests',
                'image': 'Gradient Graphic T-shirt.jpg',
                'rating': 3.5
            },
            {
                'name': 'Polo with Tipping Details',
                'description': 'Elegant polo shirt with tipping details.',
                'price': 180.00,
                'category': 'women',
                'status': 'bests',
                'image': 'Polo with Tipping Details.jpg',
                'rating': 4.5
            },
            {
                'name': 'Black Striped T-shirt',
                'description': 'Classic black striped t-shirt.',
                'price': 120.00,
                'old_price': 150.00,
                'category': 'women',
                'status': 'bests',
                'image': 'Black Striped T-shirt.jpg',
                'rating': 5.0
            },
            {
                'name': 'Vertical Striped Shirt',
                'description': 'Fashionable vertical striped shirt.',
                'price': 212.00,
                'old_price': 232.00,
                'category': 'women',
                'status': 'bests',
                'image': 'VERTICAL STRIPED .jpg',
                'rating': 5.0
            },
            {
                'name': 'Pink shirt',
                'description': 'Comfortable cotton shirt.',
                'price': 145.00,
                'category': 'women',
                'status': 'bests',
                'image': 'pink shirt.jpg',
                'rating': 4.5
            },
            {
                'name': 'Pink cap',
                'description': 'Comfortable cotton cap.',
                'price': 50.00,
                'category': 'women',
                'status': 'bests',
                'image': 'pink cap.jpg',
                'rating': 4.5
            },
            
            # Casual (6 товаров)
            {
                'name': 'Courage Graphic T-shirt',
                'description': 'Graphic t-shirt with courage design.',
                'price': 145.00,
                'category': 'casual',
                'status': '.',
                'image': 'T-COURAGE GRAPHIC .jpg',
                'rating': 4.0
            },
            {
                'name': 'Loose Fit Bermuda Shorts',
                'description': 'Comfortable loose fit bermuda shorts.',
                'price': 80.00,
                'category': 'casual',
                'status': '.',
                'image': 'LOOSE FIT BERMUDA SHORTS.jpg',
                'rating': 3.0
            },
            {
                'name': 'Faded Skinny Jeans',
                'description': 'Fashionable faded skinny jeans.',
                'price': 210.00,
                'category': 'casual',
                'status': '.',
                'image': 'Faded Skinny Jeans.jpg',
                'rating': 4.5
            },
            {
                'name': 'Orange Color T-shirt',
                'description': 'Bright orange t-shirt.',
                'price': 95.00,
                'category': 'casual',
                'status': '.',
                'image': 'T-orange_color.jpg',
                'rating': 4.2
            },
            {
                'name': 'Tommy Helfiger T-shirt',
                'description': 'Original Tommy Helfiger T-shirt',
                'price': 195.00,
                'category': 'casual',
                'status': '.',
                'image': 'Tom tailor T-shirt.jpg',
                'rating': 4.5
            },
            {
                'name': 'Balensiaga jacket',
                'description': 'balensiaga jacket.jpg',
                'price': 295.00,
                'category': 'casual',
                'status': '.',
                'image': 'balensiaga jacket.jpg',
                'rating': 5.0
            },
            
            # Новинки (4 товара)
            {
                'name': 'One Life Graphic T-shirt',
                'description': 'New collection graphic t-shirt.',
                'price': 155.00,
                'category': 'novelty',
                'status': '.',
                'image': 'T-One Life Graphic (2).jpg',
                'rating': 4.8
            },
            {
                'name': 'Polo with Contrast Trims',
                'description': 'New polo with contrast trims.',
                'price': 190.00,
                'category': 'novelty',
                'status': '.',
                'image': 'Polo with Contrast Trims.jpg',
                'rating': 4.7
            },
            {
                'name': 'Checkered Shirt',
                'description': 'Classic checkered shirt perfect for casual occasions.',
                'price': 180.00,
                'category': 'novelty',
                'status': '.',
                'image': 'CHECKERED SHIRT.jpg',
                'rating': 4.5
            },
            {
                'name': 'Sleeve Striped T-shirt',
                'description': 'Stylish striped t-shirt with unique sleeve design.',
                'price': 130.00,
                'old_price': 160.00,
                'category': 'novelty',
                'status': '.',
                'image': 'SLEEVE STRIPED.jpg',
                'rating': 4.5
            },
            
            # Спорт (6 товаров)
            {
                'name': 'Black sport T-shirt',
                'description': 'Black sport T-shirt for sportsmens',
                'price': 130.00,
                'old_price': 160.00,
                'category': 'gym',
                'status': '.',
                'image': 'Black sport T-shirt.jpg',
                'rating': 4.5
            },
            {
                'name': 'Grey sport T-shirt',
                'description': 'Grey sport T-shirt for sportsmens',
                'price': 130.00,
                'old_price': 160.00,
                'category': 'gym',
                'status': '.',
                'image': 'Grey sport T-shirt.jpg',
                'rating': 4.5
            },
            {
                'name': 'White sport T-shirt',
                'description': 'White sport T-shirt for sportsmens',
                'price': 150.00,
                'old_price': 170.00,
                'category': 'gym',
                'status': '.',
                'image': 'White sport T-shirt.jpg',
                'rating': 5.0
            },
            {
                'name': 'Puma Jacket',
                'description': 'Sport Jacket for sportsmens',
                'price': 150.00,
                'old_price': 170.00,
                'category': 'gym',
                'status': '.',
                'image': 'puma jacket.jpg',
                'rating': 4.0
            },
            {
                'name': 'Sportive long sleeved T-shirt',
                'description': 'Sportive long sleeved for sportsmens',
                'price': 160.00,
                'old_price': 180.00,
                'category': 'gym',
                'status': '.',
                'image': 'sportive long sleeved T-shirt.jpg',
                'rating': 4.0
            },
            {
                'name': 'Stussy T-shirt',
                'description': 'Original Stussy T-shirt',
                'price': 170.00,
                'old_price': 180.00,
                'category': 'gym',
                'status': '.',
                'image': 'stussy T-shirt.jpg',
                'rating': 3.5
            }
        ]
        

        added_count = 0
        for data in all_products:
            try:

                existing = Product.query.filter_by(
                    name=data['name'],
                    category=data['category']
                ).first()
                
                if not existing:
                    product = Product(**data)
                    db.session.add(product)
                    added_count += 1
                    print(f"   ✓ Added: {data['name']}")
                else:
                    print(f"   ⚠️ Already exists: {data['name']}")
                    
            except Exception as e:
                print(f"   ❌ Error adding {data['name']}: {e}")
        
        db.session.commit()
        print(f"✅ Successfully added {added_count} new products")

        total_count = Product.query.count()
        print(f"📊 Total products in database: {total_count}")

        categories = ['men', 'women', 'casual', 'novelty', 'gym']
        for category in categories:
            count = Product.query.filter_by(category=category).count()
            print(f"   {category}: {count} товаров")

with app.app_context():
    try:
        print("=" * 60)
        print("🚀 RAILWAY E-COMMERCE APP INITIALIZATION")
        print("=" * 60)

        print("\n📁 Checking filesystem access...")
        if not os.path.exists('/tmp'):
            os.makedirs('/tmp', exist_ok=True)
            print("   ✅ Created /tmp directory")

        test_file = '/tmp/railway_test.txt'
        try:
            with open(test_file, 'w') as f:
                f.write('test')
            os.remove(test_file)
            print("   ✅ Can write to /tmp")
        except Exception as e:
            print(f"   ❌ Cannot write to /tmp: {e}")

        print("\n📦 Creating database tables...")
        db.create_all()
        print("   ✅ Tables created")

        populate_initial_data()

        user_count = User.query.count()
        print(f"\n👤 Users in database: {user_count}")
        
        print("\n" + "=" * 60)
        print("✅ INITIALIZATION COMPLETED SUCCESSFULLY")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR during initialization: {e}")
        import traceback
        traceback.print_exc()
        print("=" * 60)
        print("⚠️  App may not work properly")
        print("=" * 60)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    print(f"\n🌐 Starting Flask server on port {port}")
    print(f"🔗 Database path: {app.config.get('SQLALCHEMY_DATABASE_URI')}")
    app.run(host='0.0.0.0', port=port, debug=False)