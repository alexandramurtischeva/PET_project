from __init__ import db, app


class ShoppingCart(db.Model):
    __tablename__ = 'shopping_cart'
    customer_id = db.Column(db.ForeignKey('customer_id'), primary_key=True)
    product_id = db.Column(db.ForeignKey('product_id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    customer = db.relationship('Customer', back_populates='customers')
    product = db.relationship('Product', back_populates='products')


class Customer(db.Model):
    __tablename__ = 'customer'
    id_customer = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128, nullable=False, unique=True))
    password = db.Column(db.String(128), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    customers = db.relationship('ShoppingCart', back_populates='customer')
    order = db.relationship('Order')

    def __repr__(self):
        return f'<Customer {self.name}>'


class Product(db.Model):
    __tablename__ = 'product'
    id_product = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    size = db.Column(db.String(128), nullable=False)
    color = db.Column(db.String(128), nullable=False)
    image = db.Column(db.Text, nullable=False)
    products = db.relationship('ShoppingCart', back_populates='product')

    def __repr__(self):
        return f'<Product {self.name}, {self.price}, {self.size}, {self.color} >'


class Order(db.Model):
    id_order = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Numeric(10, 2), nullable=False)
    fk_status = db.Column(db.Integer, db.ForeignKey('status.id_status'), nullable=False)
    fk_customer = db.Column(db.Integer, db.ForeignKey('customer.id_customer'), nullable=False)


class Status(db.Model):
    __tablename__ = 'status'
    id_status = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(128), nullable=False)
    order = db.relationship('Order')

    def __repr__(self):
        return f'<Status {self.status} >'

