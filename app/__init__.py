from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os

db = SQLAlchemy()

def create_app(config_class=Config):
    # Получаем абсолютный путь к папке app
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    # Путь к папке templates - она находится в той же папке, что и __init__.py
    template_dir = os.path.join(basedir, 'templates')
    
    # Путь к папке static - она также в папке app
    static_dir = os.path.join(basedir, 'static')
    
    print(f"📁 Basedir: {basedir}")
    print(f"📁 Templates dir: {template_dir}")
    print(f"📁 Static dir: {static_dir}")
    print(f"📁 Templates exists: {os.path.exists(template_dir)}")
    
    app = Flask(__name__,
                template_folder=template_dir,
                static_folder=static_dir,
                static_url_path='/static')
    
    app.config.from_object(config_class)
    
    db.init_app(app)

    from app.routes import bp
    app.register_blueprint(bp)

    return app