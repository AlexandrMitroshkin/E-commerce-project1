from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    """
    Application factory for Flask
    - Simple and clean
    - No automatic table creation (done by populate scripts)
    - Works both locally and on Render
    """

    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)

    from app.routes import bp
    app.register_blueprint(bp)

    if app.debug:
        print("=" * 50)
        print("🚀 Flask Application Initialized")
        print(f"📁 Database: {app.config['SQLALCHEMY_DATABASE_URI']}")
        print(f"🔧 Debug mode: {app.debug}")
        print("=" * 50)
    
    return app