from app import db
from app import ma
from datetime import datetime

from marshmallow_sqlalchemy import field_for
from marshmallow import fields
from werkzeug.security import generate_password_hash, check_password_hash

user_master = db.Table('user_master',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('master_id', db.Integer, db.ForeignKey('master.id'), primary_key=True)
)

user_product = db.Table('user_product',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True)
)


class TimestampMixin(object):
    created = db.Column(
        db.DateTime,  default=datetime.utcnow)
    updated = db.Column(db.DateTime)


class Master(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, default=None, unique=True)
    description = db.Column(db.String(2000), default="")
    qty = db.Column(db.Integer, default=0)
    weight = db.Column(db.Float, default=0)
    sku = db.Column(db.String(50), default=0)
    price = db.Column(db.Float, default=0)
    cost_price = db.Column(db.Float, default=0)
    product_type = db.Column(db.String(50), default="")
    tags = db.Column(db.String(500), default="")
    hsn = db.Column(db.String(500), default="")
    variants = db.Column(db.String(1000), default="")

    def __init__(self, name, description, qty, weight, sku, price, cost_price, product_type, tags, hsn, variants):
        self.name = name
        self.description = description
        self.qty = qty
        self.weight = weight
        self.sku = sku
        self.price = price
        self.cost_price = cost_price
        self.product_type = product_type
        self.tags = tags
        self.hsn = hsn
        self.variants = variants


class MasterSchema(ma.ModelSchema):
    id = field_for(Master, 'id', dump_only=True)
    name = field_for(Master, 'name', dump_only=True)
    description = field_for(Master, 'description', dump_only=True)
    qty = field_for(Master, 'qty', dump_only=True)
    weight = field_for(Master, 'weight', dump_only=True)
    sku = field_for(Master, 'sku', dump_only=True)
    price = field_for(Master, 'price', dump_only=True)
    cost_price = field_for(Master, 'cost_price', dump_only=True)
    product_type = field_for(Master, 'product_type', dump_only=True)
    tags = field_for(Master, 'tags', dump_only=True)
    hsn = field_for(Master, 'hsn', dump_only=True)
    variants = field_for(Master, 'variants', dump_only=True)

    class meta:
        model = Master



class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(100), default="")
    product_id = db.Column(db.String(100), default="", nullable=False)

    def __init__(self, product_id):
        self.product_id = product_id



class User(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    username = db.Column(db.String(50), unique=True)
    firm_name = db.Column(db.String(50))
    firm_phone = db.Column(db.String(50))
    firm_gst = db.Column(db.String(50))
    firm_address = db.Column(db.String(500))
    image = db.Column(db.String(100))
    order_start = db.Column(db.Integer)
    password_hash = db.Column(db.String(250))
    shop_url = db.Column(db.String(250), default="")
    shop_name = db.Column(db.String(50), default="")
    masters = db.relationship('Master', secondary=user_master, lazy='subquery',
        backref=db.backref('user', lazy=True))
    products = db.relationship('Products', secondary=user_product, lazy='subquery',
        backref=db.backref('user_prod', lazy=True))
    
    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class UserSchema(ma.ModelSchema):
    firm_name = field_for(User, 'firm_name', dump_only=True)
    firm_phone = field_for(User, 'firm_phone', dump_only=True)
    firm_gst = field_for(User, 'firm_gst', dump_only=True)
    firm_address = field_for(User, 'firm_address', dump_only=True)
    order_start = field_for(User, 'order_start', dump_only=True)
    image = field_for(User, 'image', dump_only=True)
    class meta:
        model = User

class Orders(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    shopify_order_id = db.Column(db.String(50), unique=True)
    firm_order_id = db.Column(db.String(50), unique=True)
    shipping_rate = db.Column(db.String(5))
    shipping_tax = db.Column(db.String(5))
    inv_date = db.Column(db.DateTime)
    order_type = db.Column(db.String(10))
    customer_name = db.Column(db.String(50))
    customer_address = db.Column(db.String(1000))
    customer_phone = db.Column(db.String(20))
    customer_email = db.Column(db.String(100))
    customer_gst = db.Column(db.String(25), default="")
    shipping_address = db.Column(db.String(1000))
    total_bill = db.Column(db.String(50))
    status = db.Column(db.String(15), default="pending")

    item = db.relationship("Item",
                           back_populates="orders")
    # masters = db.relationship('Master', secondary=user_master, lazy='subquery',
    #     backref=db.backref('user', lazy=True))

class Item(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(50))
    unq_item_id = db.Column(db.String(50))
    name = db.Column(db.String(250))

    orders_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    orders = db.relationship("Orders", back_populates="item", lazy="joined")

    
    qty = db.Column(db.Float, nullable=False, default=1)
    price = db.Column(db.Float, nullable=False, default=0)
    tax = db.Column(db.Float, default=0)
    discount = db.Column(db.Float, default=0)
    hsn = db.Column(db.String(10), default="")
    meta = db.Column(db.String(150), default="{}")

    def __init__(self , product_id , unq_item_id ,name,qty,price,tax,discount,hsn):
        self.product_id = product_id
        self.unq_item_id = unq_item_id
        self.name = name
        self.qty = qty
        self.price = price
        self.tax = tax
        self.discount = discount
        self.hsn = hsn

class ItemSchema(ma.ModelSchema):
    name = field_for(Item, 'name', dump_only=True)
    qty = field_for(Item, 'qty', dump_only=True)
    price = field_for(Item, 'price', dump_only=True)
    tax = field_for(Item, 'tax', dump_only=True)
    discount = field_for(Item, 'discount', dump_only=True)
    hsn = field_for(Item, 'hsn', dump_only=True)

    class meta:
        model=Item

class OrdersSchema(ma.ModelSchema):
    shopify_order_id = field_for(Orders, 'shopify_order_id', dump_only=True)
    firm_order_id = field_for(Orders, 'firm_order_id', dump_only=True)
    shipping_rate = field_for(Orders, 'shipping_rate', dump_only=True)
    shipping_tax = field_for(Orders, 'shipping_tax', dump_only=True)
    inv_date = field_for(Orders, 'inv_date', dump_only=True)
    order_type = field_for(Orders, 'order_type', dump_only=True)
    customer_name = field_for(Orders, 'customer_name', dump_only=True)
    customer_address = field_for(Orders, 'customer_address', dump_only=True)
    customer_phone = field_for(Orders, 'customer_phone', dump_only=True)
    customer_email = field_for(Orders, 'customer_email', dump_only=True)
    customer_gst = field_for(Orders, 'customer_gst', dump_only=True)
    shipping_address = field_for(Orders, 'shipping_address', dump_only=True)
    total_bill = field_for(Orders, 'total_bill', dump_only=True)
    status = field_for(Orders, 'status', dump_only=True)
    item = ma.Nested(ItemSchema(many=True))
    class meta:
        model=Orders
    
'''

    Order Model

    Primary ID - Shopify Order Nuumber is unique
    itminan Order ID - My order number -
    shipping rate
    shipping tax
    customer address
    customer phone
    customer email
    customer name
    net bill
    Product -> 
            -> product_id
            -> price
            -> discount
            -> tax

'''