from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from werkzeug.security import check_password_hash

from .forms import productForm
from ..models import Product, User, db, cart
from ..services import findproduct

products = Blueprint('products', __name__, template_folder='products_templates')

# @products.route('/products', methods=['GET', 'POST'])
# def product():
#     form = productForm()
#     my_list = range(1, 20)
#     product_list = []
#     for i in my_list:
#         product = findproduct(i)
#         if product:
#             name = product['Name']
#             price = product['Price']
#             description = product['Description']
#             img_url = product['img_url']
#             category = product['Category']
#             rating = product['Rating']
#             image_1 = product['image_1']
#             item = Product(name, price, description, img_url, category, rating, image_1)
#             item.saveProduct()
#             product_list.append(item)
#     return render_template('product.html', form=form, product_list=product_list)

    # if 'more_info' in request.form:
    #     product = findproduct(request.form['more_info'])
    #     return render_template('single_product.html', form=form, product=product)
    # elif 'add_to_cart' in request.form:        
    #     product = findproduct(request.form['add_to_cart'])
    #     name = product['Name']
    #     price = product['Price']
    #     description = product['Description']
    #     img_url = product['img_url']
    #     category = product['Category']
    #     rating = product['Rating']
    #     user_id = current_user.id
    #     item = Product(name, price, description, img_url, category, rating, user_id)
    #     item.saveProduct()
    #     flash(f'{product["Name"]} added to cart')


@products.route('/products', methods=['GET', 'POST'])
def product():
    form = productForm()
    my_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11','12','13','14','15','16','17','18','19']
    product_list = []
    for i in my_list:
        product_list.append(Product.query.filter_by(id=i).first())
    return render_template('products.html', form=form, product_list=product_list)

@products.route('/single_product/<int:product_id>')
def single_product(product_id):
    product = Product.query.get(product_id)
    return render_template('single_product.html', product=product)

@products.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = Product.query.get(product_id)
    current_user.cart.append(product)
    db.session.commit()
    flash(f'{product.name} added to cart', 'warning')
    return redirect(url_for('products.product'))

@products.route('/cart/remove/<int:product_id>')
def remove(product_id):
    product = Product.query.get(product_id)
    current_user.cart.remove(product)
    db.session.commit()
    flash(f'{product.name} removed from cart', 'danger')
    return redirect(url_for('products.cart'))

@products.route('/cart')
def cart():
    products = current_user.cart
    total = 0
    for product in products:
        total += int(product.price)
    return render_template('cart.html', products=products , total=total)

@products.route('/remove_all')
def remove_all():
    products = current_user.cart
    for product in products:
        products.remove(product)
    db.session.commit()
    return redirect(url_for('products.cart',products=products))

# @products.route('/cart/add/<int:product_id>')
# def add_to_cart(p_id):
#     p_id = current_user.cart.product_id
#     p_count = p_id.count()
#     return redirect(url_for('products.product', count = p_count))