from app import db
from app import ma
from datetime import datetime

from marshmallow_sqlalchemy import field_for
from marshmallow import fields


class Master(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50) , nullable= False , default= None , unique= True)
    description = db.Column(db.String(2000) , default="")
    qty = db.Column(db.Integer , default=0)
    weight = db.Column(db.Float , default=0)
    sku = db.Column(db.String(50) , default=0)
    price = db.Column(db.Float , default=0)
    cost_price = db.Column(db.Float , default=0)
    product_type = db.Column(db.String(50) , default="")
    tags = db.Column(db.String(500), default="")
    
    def __init__(self , name , description , qty , weight ,sku , price , cost_price, product_type , tags):
        self.name = name
        self.description = description
        self.qty = qty
        self.weight = weight
        self.sku = sku
        self.price = price
        self.cost_price = cost_price
        self.product_type = product_type
        self.tags = tags

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


    class meta:
        model = Master

# SKU's generated based on SKU + ID 
