import os

print("🚀 Исправляем ошибку Render...")

# 1. Создаем app.py
app_py_content = '''import os
from app import create_app

# Создаем приложение
app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
'''

with open('app.py', 'w') as f:
    f.write(app_py_content)
print("✅ app.py создан")

# 2. Обновляем render.yaml
render_yaml = '''services:
  - type: web
    name: ecommerce-shop
    env: python
    region: frankfurt
    plan: free
    branch: main
    buildCommand: |
      pip install --upgrade pip
      pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: FLASK_APP
        value: app.py
      - key: SECRET_KEY
        generateValue: true
      - key: DATABASE_URL
        value: sqlite:///shop.db
    healthCheckPath: /
    autoDeploy: true
'''

with open('render.yaml', 'w') as f:
    f.write(render_yaml)
print("✅ render.yaml обновлен")

# 3. Обновляем requirements.txt
requirements = '''Flask==2.3.2
Flask-SQLAlchemy==3.0.3
python-dotenv==1.0.0
gunicorn==20.1.0
'''

with open('requirements.txt', 'w') as f:
    f.write(requirements)
print("✅ requirements.txt обновлен")

# 4. Удаляем wsgi.py если есть
if os.path.exists('wsgi.py'):
    os.remove('wsgi.py')
    print("✅ wsgi.py удален")

# 5. Проверяем run.py (можно оставить или удалить)
if os.path.exists('run.py'):
    print("ℹ️  run.py остался (нужен для локального запуска)")

print("\n🎯 Исправления применены!")
print("Теперь выполни:")
print("1. git add .")
print("2. git commit -m 'Fix: app.py for Render'")
print("3. git push")
print("4. Render автоматически перезапустится")