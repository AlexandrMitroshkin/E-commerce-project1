import os
import sys
from pathlib import Path

# Добавляем корень проекта в путь Python
project_root = Path('/opt/render/project/src')
sys.path.insert(0, str(project_root))

from app import create_app, db
from app.models import Product, User
from datetime import datetime

def init_database():
    print("Initializing database on Render...")
    
    app = create_app()
    
    with app.app_context():
        # Создаем папку instance если ее нет
        instance_dir = project_root / 'instance'
        instance_dir.mkdir(exist_ok=True)
        
        print(f"Creating database at: {instance_dir}/shop.db")
        
        # Создаем таблицы
        db.create_all()
        print("Database tables created successfully!")
        
        # Проверяем, есть ли уже данные
        if Product.query.count() == 0:
            print("No products found, populating database...")
            # Импортируем и запускаем populate_db
            from populate_db import test_products
            
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
            print(f"Added {len(test_products)} test products to database!")
        else:
            print(f"Database already contains {Product.query.count()} products")

if __name__ == '__main__':
    init_database()