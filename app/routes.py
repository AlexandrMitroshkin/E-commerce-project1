from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import User, db

bp = Blueprint('main', __name__)

# ===== ГЛАВНЫЕ СТРАНИЦЫ =====
@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/product/<int:id>')
def product(id):
    return render_template('product.html', product_id=id)

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