import os

print("🚀 Подготавливаем для Render.com...")

# 1. requirements.txt
with open('requirements.txt', 'w') as f:
    f.write("""Flask==2.3.2
Flask-SQLAlchemy==3.0.3
python-dotenv==1.0.0
gunicorn==20.1.0
""")
print("✅ requirements.txt")

# 2. render.yaml
with open('render.yaml', 'w') as f:
    f.write("""services:
  - type: web
    name: ecommerce-shop
    env: python
    region: frankfurt
    plan: free
    branch: main
    buildCommand: |
      pip install --upgrade pip
      pip install -r requirements.txt
    startCommand: gunicorn run:app
    envVars:
      - key: FLASK_APP
        value: run.py
      - key: SECRET_KEY
        generateValue: true
      - key: DATABASE_URL
        value: sqlite:///shop.db
    healthCheckPath: /
    autoDeploy: true
""")
print("✅ render.yaml")

# 3. wsgi.py
with open('wsgi.py', 'w') as f:
    f.write("""from run import app

if __name__ == "__main__":
    app.run()
""")
print("✅ wsgi.py")

# 4. Обновляем run.py
with open('run.py', 'w') as f:
    f.write("""import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
""")
print("✅ run.py обновлен")

print("\n🎯 Готово! Теперь:")
print("1. git add .")
print("2. git commit -m 'Prepare for Render'")
print("3. git push")
print("4. Иди на render.com")