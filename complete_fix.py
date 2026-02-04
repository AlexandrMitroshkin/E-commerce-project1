import os
import shutil

print("🚀 ПОЛНЫЙ ФИКС ДЛЯ RENDER...")

# 1. Удаляем старые файлы которые мешают
files_to_remove = ['app.py', 'wsgi.py', 'Procfile']
for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
        print(f"✅ Удален: {file}")

# 2. Создаем application.py
app_content = '''"""
Главный файл приложения для Render
"""
import os
from app import create_app

# СОЗДАЕМ ПЕРЕМЕННУЮ app - ОНА НУЖНА ДЛЯ GUNICORN!
app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
'''

with open('application.py', 'w') as f:
    f.write(app_content)
print("✅ Создан: application.py")

# 3. Обновляем run.py (для локального запуска)
run_content = '''"""
Локальный запуск
"""
import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
'''

with open('run.py', 'w') as f:
    f.write(run_content)
print("✅ Обновлен: run.py")

# 4. СОЗДАЕМ НОВЫЙ render.yaml с правильной командой
render_yaml = '''# Render конфигурация
services:
  - type: web
    name: ecommerce-shop
    env: python
    region: frankfurt
    plan: free
    branch: main
    buildCommand: |
      pip install --upgrade pip
      pip install -r requirements.txt
    # ВАЖНО! Используем application:app
    startCommand: gunicorn application:app
    envVars:
      - key: FLASK_APP
        value: application.py
      - key: SECRET_KEY
        generateValue: true
      - key: DATABASE_URL
        value: sqlite:///shop.db
    healthCheckPath: /
    autoDeploy: true
'''

with open('render.yaml', 'w') as f:
    f.write(render_yaml)
print("✅ Создан: render.yaml")

# 5. Обновляем requirements.txt
requirements = '''Flask==2.3.2
Flask-SQLAlchemy==3.0.3
python-dotenv==1.0.0
gunicorn==20.1.0
Werkzeug==2.3.0
'''

with open('requirements.txt', 'w') as f:
    f.write(requirements)
print("✅ Обновлен: requirements.txt")

# 6. Проверяем app/__init__.py
init_path = 'app/__init__.py'
if os.path.exists(init_path):
    with open(init_path, 'r') as f:
        content = f.read()
    if 'def create_app' in content:
        print("✅ app/__init__.py содержит create_app()")
    else:
        print("❌ app/__init__.py НЕ содержит create_app()!")
else:
    print("❌ app/__init__.py не найден!")

print("\n" + "="*50)
print("🎯 ВСЕ ФАЙЛЫ ГОТОВЫ!")
print("="*50)
print("\nТеперь выполни:")
print("1. git add .")
print("2. git commit -m 'Complete fix for Render'")
print("3. git push origin main")
print("\nЗатем зайди на render.com и:")
print("1. Открой свой проект ecommerce-shop")
print("2. Нажми 'Manual Deploy' → 'Clear cache and deploy'")
print("3. Жди 5 минут")
print("\n🌐 Ссылка будет: https://ecommerce-shop.onrender.com")