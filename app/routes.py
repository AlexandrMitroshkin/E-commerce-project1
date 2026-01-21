from flask import Blueprint, render_template
# from app.models import Product

bp = Blueprint('main', __name__)

# Blueprint у меня сдесь плохо использован подкорректуй

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/product/<int:id>')
def product(id):
    return render_template('product.html', product_id=id)
  
@bp.route('/casual')
def casual():
    return render_template('casual.html')

@bp.route('/cart')
def cart(): 
    return render_template('cart.html')

@bp.route('/men')
def men():
    return render_template('men.html')

@bp.route('/women')
def women():
    return render_template('women.html')

@bp.route('/unisex')
def unisex():
    return render_template('unisex.html')

@bp.route('/combined')
def combined():
    return render_template('combined.html')

@bp.route('/sales')
def sales():
    return render_template('sales.html')

@bp.route('/novelty')
def novelty():
    return render_template('novelty.html')

@bp.route('/brands')
def brands():
    return render_template('brands.html')

@bp.route('/account')
def account():
    return render_template('account.html')
