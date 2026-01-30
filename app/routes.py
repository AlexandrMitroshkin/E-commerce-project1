from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import User, Product, db

bp = Blueprint('main', __name__)

# ===== ГЛАВНАЯ СТРАНИЦА =====
@bp.route('/')
def home():
    # Получаем товары для главной страницы
    new_arrivals = Product.query.filter_by(category='men').limit(4).all()
    top_selling = Product.query.filter_by(category='women').limit(4).all()
    
    return render_template('home.html', 
                         new_arrivals=new_arrivals, 
                         top_selling=top_selling)

# ===== УНИВЕРСАЛЬНАЯ СТРАНИЦА КАТЕГОРИИ =====
@bp.route('/category/<category_name>')
def category(category_name):
    # Имена категорий для отображения
    display_names = {
        'men': 'Men',
        'women': 'Women', 
        'casual': 'Casual',
        'unisex': 'Unisex',
        'novelty': 'New Arrivals',
        'sales': 'Sale'
    }
    
    display_name = display_names.get(category_name, category_name.capitalize())
    
    # Для распродажи фильтруем по старой цене
    if category_name == 'sales':
        products = Product.query.filter(Product.old_price.isnot(None)).all()
    else:
        products = Product.query.filter_by(category=category_name).all()
    
    return render_template(
        'category_base.html',
        category_name=display_name,
        category_slug=category_name,
        products=products,
        total_count=len(products)
    )

# ===== СТРАНИЦА ТОВАРА =====
@bp.route('/product/<int:id>')
def product(id):
    product = Product.query.get_or_404(id)
    return render_template('product.html', product=product)

# ===== ПЕРЕАДРЕСАЦИЯ СТАРЫХ МАРШРУТОВ =====
@bp.route('/men')
def men():
    return redirect(url_for('main.category', category_name='men'))

@bp.route('/women')
def women():
    return redirect(url_for('main.category', category_name='women'))

@bp.route('/casual')
def casual():
    return redirect(url_for('main.category', category_name='casual'))

@bp.route('/unisex')
def unisex():
    return redirect(url_for('main.category', category_name='unisex'))

@bp.route('/novelty')
def novelty():
    return redirect(url_for('main.category', category_name='novelty'))

@bp.route('/sales')
def sales():
    return redirect(url_for('main.category', category_name='sales'))

# ===== АВТОРИЗАЦИЯ =====
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('main.account'))
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('This name is already taken!', 'error')
            return redirect(url_for('main.register'))
        
        user = User(username=username, email=email)
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        session['user_id'] = user.id
        session['username'] = user.username
        
        flash('Registration successful!', 'success')
        return redirect(url_for('main.account'))
    
    return render_template('register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('main.account'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('main.account'))
        else:
            flash('Incorrect username or password', 'error')
            return redirect(url_for('main.login'))
    
    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.clear()
    flash('You are logged out', 'info')
    return redirect(url_for('main.home'))

@bp.route('/account')
def account():
    if 'user_id' not in session:
        flash('Please log in', 'error')
        return redirect(url_for('main.login'))
    
    user = User.query.get(session['user_id'])
    return render_template('account.html', user=user)

# ===== ОСТАЛЬНЫЕ СТРАНИЦЫ =====
@bp.route('/cart')
def cart(): 
    return render_template('cart.html')

@bp.route('/combined')
def combined():
    return render_template('combined.html')

@bp.route('/brands')
def brands():
    return render_template('brands.html')