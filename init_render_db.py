#!/usr/bin/env python3
"""
Создание базы данных на Render
"""

print("=" * 60)
print("🚀 INIT_RENDER_DB.PY STARTED")
print("=" * 60)

# 1. Сначала создаем файл базы данных
import sqlite3
import os

print("📁 Creating database file...")
db_path = '/tmp/shop.db'

try:
    # Удаляем старый файл если есть
    if os.path.exists(db_path):
        os.remove(db_path)
        print("🗑️  Removed old database file")
    
    # Создаем новую базу данных
    conn = sqlite3.connect(db_path)
    conn.close()
    print(f"✅ Database file created at: {db_path}")
except Exception as e:
    print(f"❌ Error creating database file: {e}")
    exit(1)

# 2. Теперь создаем таблицы через Flask
print("📦 Creating database tables...")
try:
    # Импортируем после создания файла БД
    from app import create_app, db
    
    app = create_app()
    
    with app.app_context():
        # Создаем все таблицы
        db.create_all()
        print("✅ Database tables created successfully!")
        
        # Проверяем таблицу product
        from app.models import Product
        from sqlalchemy import inspect
        
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        print(f"📊 Tables in database: {tables}")
        
        # Добавляем тестовые данные
        if 'product' in tables:
            print("📥 Adding test products...")
            
            # Добавляем один тестовый товар
            test_product = Product(
                name="Test T-shirt",
                description="Test product for Render deployment",
                price=99.99,
                category="men",
                status="bests",
                image="T-TAPE DETAILS.jpg",
                rating=4.5
            )
            
            db.session.add(test_product)
            db.session.commit()
            print("✅ Test product added successfully!")
            
            # Проверяем
            product_count = Product.query.count()
            print(f"📊 Total products in database: {product_count}")
        else:
            print("⚠️  Table 'product' not found!")
            
except Exception as e:
    print(f"❌ Error creating tables: {e}")
    import traceback
    traceback.print_exc()

print("=" * 60)
print("✅ INIT_RENDER_DB.PY COMPLETED")
print("=" * 60)     