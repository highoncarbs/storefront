import logging
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate
import shopify

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

from model import Master, MasterSchema

SHOP_URL = 'https://c5673965f8cef9f48d175bad834a39aa:ad4fd2c761999a71e58d3b22884cbef5@highoncarbs.myshopify.com/admin/api/2019-10/'
shopify.ShopifyResource.set_site(SHOP_URL)
shop = shopify.Shop.current()

import products

@app.route('/get/products', methods=['GET'])
def get_products():
    data = requests.get(SHOP_URL + str('products.json'))
    return data.json()


@app.route('/add/master', methods=['POST'])
def add_master():
    payload = request.json
    if payload is not None:
        try:
            new_data = Master(payload['title'], payload['description'],
                              payload['qty'], payload['weight'],  payload['sku'],   payload['price'], payload['cost_price'],  payload['type'], payload['tags'] ,  payload['hsn'])
            db.session.add(new_data)
            db.session.commit()
            return jsonify({'success': 'Data Added'})

        except IntegrityError as e:
            print(e)
            return jsonify({'message': 'Duplicate Data'})
        except Exception as e:
            print(e)
            return jsonify({'message': 'Data Entry Error'})
    return jsonify({'message': 'Empty request'})


@app.route('/get/master', methods=['GET'])
def get_master():
    schema = MasterSchema(many=True)
    data = Master.query.all()
    return jsonify(schema.dump(data))


# Flow -> Create Porduct with Base Details -> get Product ID -> UPdate Inventory Level ( cost , sku )-> Return adn Add to local database .
# 
