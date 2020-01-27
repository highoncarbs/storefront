from app import db
from app import ma
from datetime import datetime

from marshmallow_sqlalchemy import field_for
from marshmallow import fields


class Master(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50) , nullable= False , default= None , unique= True)
    description = db.Column(db.String(1000) , default="")
    qty = db.Column(db.Integer , default=0)
    weight = db.Column(db.Float , default=0)
    sku = db.Column(db.Float , default=0)
    price = db.Column(db.Float , default=0)
    cost_price = db.Column(db.Float , default=0)
    product_type = db.Column(db.String(50) , default="")
    tags = db.Column(db.String(500), default="")
    
class MasterSchema(ma.ModelSchema):
    class meta:
        model = Master

# SKU's generated based on SKU + ID 
