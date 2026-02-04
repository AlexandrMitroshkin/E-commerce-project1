import os
from pathlib import Path

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'rBas3mf8956feiWcxjK9qP8UB-hw5K0ho5AZajWQI6U'
    
    if os.environ.get('RENDER'):
        BASE_DIR = Path('/opt/render/project/src')
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{BASE_DIR}/instance/shop.db'
    else:
        BASE_DIR = Path(__file__).resolve().parent
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{BASE_DIR}/instance/shop.db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
