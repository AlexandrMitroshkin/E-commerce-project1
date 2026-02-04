import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'rBas3mf8956feiWcxjK9qP8UB-hw5K0ho5AZajWQI6U'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///shop.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False