from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.routes import bp
    app.register_blueprint(bp)

    with app.app_context():
        try:
            # Пробуем создать таблицы, но не падаем если не получится
            db.create_all()
            print("✅ Database tables created successfully!")
        except Exception as e:
            print(f"⚠️  Database initialization warning: {e}")
            print("Tables will be created when needed...")

    return app