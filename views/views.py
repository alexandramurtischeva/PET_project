from flask import render_template
from flask_classy import FlaskView, route

class MainView(FlaskView):

    route_base = '/'

    @route('/')
    def index(self):
        return render_template('index.html')

class ProductView(FlaskView):
    route_base = '/'
    @route('/products')
    def products(self):
        return render_template('catalogue.html')

    @route('/products/add', endpoint='add_product')
    def add_product(self):
        return render_template('catalogue.html')

    @route('/products/update', endpoint='update_product')
    @route('/products/update/<product_id>', endpoint='update_product')
    def update_product(self, product_id=None):
        return render_template('catalogue.html')

    @route('/products/delete', endpoint='delete_product')
    @route('/products/delete/<product_id>', endpoint='delete_product')
    def delete_product(self, product_id=None):
        return render_template('catalogue.html')

class ShoppingView(FlaskView):
    route_base = '/'
    @route('/shopping_cart')
    def shopping_cart(self):
        return render_template('shopping_cart.html')


class CustomerView(FlaskView):
    route_base = '/'
    @route('/login', endpoint='login')
    def log_in(self):
        return render_template('login.html')

    @route('/sign_up')
    def sign_up(self):
        return render_template('sign_up.html')


