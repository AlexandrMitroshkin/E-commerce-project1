from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from app.models import User, Product, db, CartItem

bp = Blueprint('main', __name__)


@bp.route('/')
def home():
    try:
        new_arrivals = Product.query.filter_by(category='novelty').limit(8).all()
        top_selling = Product.query.filter_by(status='bests').limit(8).all()
    except Exception as e:
        print(f"⚠️  Ошибка базы данных: {e}")
        new_arrivals = []
        top_selling = []
    
    return render_template('home.html', 
                         new_arrivals=new_arrivals, 
                         top_selling=top_selling)


@bp.route('/category/<category_name>')
def category(category_name):

    display_names = {
        'men': 'Men',
        'women': 'Women', 
        'casual': 'Casual',
        'unisex': 'Unisex',
        'novelty': 'New Arrivals',
        'sales': 'Sale',
        'bests': 'Top Selling',
        'gym':'Gym'
    }
    
    display_name = display_names.get(category_name, category_name.capitalize())
    

    if category_name == 'sales':

        products = Product.query.filter(Product.old_price.isnot(None)).all()
    elif category_name == 'bests':

        products = Product.query.filter_by(status='bests').all()
    elif category_name == 'novelty':

        products = Product.query.filter_by(category='novelty').all()
    elif category_name == 'gym':
        products = Product.query.filter_by(category='gym').all()
    else:

        products = Product.query.filter_by(category=category_name).all()
    
    return render_template(
        'category_base.html',
        category_name=display_name,
        category_slug=category_name,
        products=products,
        total_count=len(products)
    )


@bp.route('/product/<int:id>')
def product(id):
    product = Product.query.get_or_404(id)
    return render_template('product.html', product=product)


@bp.route('/men')
def men():
    return redirect(url_for('main.category', category_name='men'))

@bp.route('/women')
def women():
    return redirect(url_for('main.category', category_name='women'))

@bp.route('/casual')
def casual():
    return redirect(url_for('main.category', category_name='casual'))

@bp.route('/novelty')
def novelty():
    return redirect(url_for('main.category', category_name='novelty'))

@bp.route('/sales')
def sales():
    return redirect(url_for('main.category', category_name='sales'))

@bp.route('/bests')
def bests():
    return redirect(url_for('main.category', category_name='bests'))

@bp.route('/gym')
def gym():
    return redirect(url_for('main.category', category_name='gym'))



@bp.route('/add-to-cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    """Добавить товар в корзину"""
    if 'user_id' not in session:
        return jsonify({
            'success': False, 
            'redirect': url_for('main.login')
        })
    
    product = Product.query.get_or_404(product_id)
    
  
    cart_item = CartItem.query.filter_by(
        user_id=session['user_id'],
        product_id=product_id
    ).first()
    
    if cart_item:
        cart_item.quantity += 1
        message = f'{product.name} quantity updated'
    else:
        cart_item = CartItem(
            user_id=session['user_id'],
            product_id=product_id,
            quantity=1
        )
        db.session.add(cart_item)
        message = f'{product.name} added to cart'
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': message
    })

@bp.route('/cart')
def cart():
    """Страница корзины"""
    if 'user_id' not in session:
        flash('Please login to view your cart', 'error')
        return redirect(url_for('main.login'))
    
    cart_items = CartItem.query.filter_by(user_id=session['user_id']).all()
    

    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    delivery = 15.00 if cart_items else 0
    total = subtotal + delivery
    
    return render_template('cart.html', 
                         cart_items=cart_items,
                         subtotal=subtotal,
                         delivery=delivery,
                         total=total)

@bp.route('/update-cart/<int:item_id>', methods=['POST'])
def update_cart(item_id):
    """Изменить количество"""
    if 'user_id' not in session:
        return jsonify({'success': False})
    
    cart_item = CartItem.query.get_or_404(item_id)
    
    if cart_item.user_id != session['user_id']:
        return jsonify({'success': False})
    
    action = request.json.get('action')
    
    if action == 'increase':
        cart_item.quantity += 1
    elif action == 'decrease' and cart_item.quantity > 1:
        cart_item.quantity -= 1
    elif action == 'remove':
        db.session.delete(cart_item)
    else:
        return jsonify({'success': False})
    
    db.session.commit()
    

    cart_items = CartItem.query.filter_by(user_id=session['user_id']).all()
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    delivery = 15.00 if cart_items else 0
    total = subtotal + delivery
    
    return jsonify({
        'success': True,
        'subtotal': subtotal,
        'delivery': delivery,
        'total': total,
        'quantity': cart_item.quantity if cart_item.quantity > 0 else 0
    })


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


@bp.route('/search-products')
def search_products():
    query = request.args.get('q', '').strip()
    
    if not query:
        return jsonify([])
    
    products = Product.query.filter(
        Product.name.ilike(f'%{query}%')
    ).limit(10).all()
    
    results = []
    for product in products:
        results.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'category': product.category,
            'url': url_for('main.product', id=product.id)
        })
    
    return jsonify(results)

@bp.route('/under-construction')
def under_construction():
    return render_template('under_construction.html')

@bp.route('/combined')
def combined():
    return render_template('combined.html')

@bp.route('/brands')
def brands():
    return render_template('brands.html')

@bp.route('/stub')
def stub():
    return render_template('stub.html')