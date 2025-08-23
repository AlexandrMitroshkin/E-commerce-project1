from flask import Blueprint, render_template
from app.models import Product

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/product/<int:id>')
def product():
    return render_template('product.html')
  
@bp.route('/Casual')
def Casual():
    return render_template('Casual.html')

@bp.route('/Cart')
def Cart(): 
    return render_template('Cart.html')

@bp.route('/Men')
def Men():
    return render_template('Men.html')

@bp.route('/Women')
def Women():
    return render_template('Women.html')

@bp.route('/Unisex')
def Unisex():
    return render_template('Unisex.html')

@bp.route('/Combined')
def Combined():
    return render_template('Combined.html')

@bp.route('/Sales')
def Sales():
    return render_template('Sales.html')

@bp.route('/Novelty')
def Novelty():
    return render_template('Novelty.html')

@bp.route('/Brands')
def Brands():
    return render_template('Brands.html')

@bp.route('/Account')
def Account():
    return render_template('Account.html')
