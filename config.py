import os

class Config:
    SECRET_KEY = '1NZqsu3leV43JS4o6VlY'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///shop.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False