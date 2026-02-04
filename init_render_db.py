
"""
init_render_db.py - Создает базу данных на Render
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    from app import create_app, db
    from app.models import Product
    print("✅ Модули успешно импортированы")
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    sys.exit(1)

def main():
    print("=" * 60)
    print("🚀 НАЧАЛО СОЗДАНИЯ БАЗЫ ДАННЫХ НА RENDER")
    print("=" * 60)
    
    try:

        app = create_app()
        print(f"✅ Приложение создано")
        print(f"📁 Путь к БД: {app.config['SQLALCHEMY_DATABASE_URI']}")
        
        with app.app_context():

            print("📦 Создаем таблицы...")
            db.create_all()
            print("✅ Таблицы созданы успешно!")
            

            try:
                count = Product.query.count()
                print(f"📊 В таблице product: {count} записей")
            except:
                print("⚠️  Таблица product пуста или недоступна")
            

            try:
                if Product.query.count() == 0:
                    print("📥 Добавляем тестовые товары...")
                    

                    products = [
                        Product(
                            name="Test T-shirt",
                            description="Test product for Render",
                            price=99.99,
                            category="men",
                            status="bests",
                            image="T-TAPE DETAILS.jpg",
                            rating=4.5
                        ),
                        Product(
                            name="Test Jeans",
                            description="Another test product",
                            price=149.99,
                            category="men",
                            status="bests",
                            image="SKINNY FIT JEANS.jpg",
                            rating=4.0
                        )
                    ]
                    
                    for product in products:
                        db.session.add(product)
                    
                    db.session.commit()
                    print(f"✅ Добавлено {len(products)} тестовых товара")
                else:
                    print("✅ В базе уже есть товары")
            except Exception as e:
                print(f"⚠️  Ошибка при добавлении товаров: {e}")
                db.session.rollback()
    
    except Exception as e:
        print(f"❌ КРИТИЧЕСКАЯ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    print("=" * 60)
    print("✅ БАЗА ДАННЫХ УСПЕШНО СОЗДАНА НА RENDER")
    print("=" * 60)

if __name__ == "__main__":
    main()