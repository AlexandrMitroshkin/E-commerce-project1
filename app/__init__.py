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
            db.create_all()
            print("✅ Database tables are ready")
        except Exception as e:
            print(f"⚠️  Database warning: {e}")
    
    return app