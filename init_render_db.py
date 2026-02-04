import os
import sys
from pathlib import Path


current_dir = Path(__file__).parent
project_root = current_dir


sys.path.insert(0, str(project_root))

from app import create_app, db
from app.models import Product, User
from datetime import datetime

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

]

def init_database():
    print("🚀 Initializing database...")
    
    try:
        app = create_app()
    except Exception as e:
        print(f"❌ Error creating app: {e}")
        sys.exit(1)
    
    with app.app_context():
        try:

            instance_dir = project_root / 'instance'
            instance_dir.mkdir(exist_ok=True)
            
            print(f"📁 Database path: {app.config['SQLALCHEMY_DATABASE_URI']}")
            
 
            db.create_all()
            print("✅ Database tables created successfully!")
            

            product_count = Product.query.count()
            print(f"📊 Current product count: {product_count}")
            
            if product_count == 0:
                print("📦 No products found, populating database...")
                
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
                print(f"✅ Added {len(test_products)} test products to database!")
            else:
                print(f"✅ Database already contains {product_count} products")
                
        except Exception as e:
            print(f"❌ Database initialization failed: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)

if __name__ == '__main__':
    init_database()