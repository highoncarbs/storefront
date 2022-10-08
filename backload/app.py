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
from flask_jwt_extended import JWTManager , jwt_required , get_jwt_identity
from config import SHOP_URL


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from model import Master, MasterSchema , User , Colour , Craft , Fabric , Tags

import products , auth , orders 

@app.route('/get/products', methods=['GET'])
@jwt_required
def get_products():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()
    print(user.shop_url)
    if(user.shop_url != ""):
        data = requests.get(user.shop_url + str('products.json'))
        return jsonify({'success' : 'Products loaded' , 'data': data.json() })
    else:
        return jsonify({'message' : 'SHOP URL not defined. Add one in Settings'})


@app.route('/add/master', methods=['POST'])
@jwt_required
def add_master():
    payload = request.json
    if payload is not None:
        try:
            current_user = get_jwt_identity()
            user = User.query.filter_by( username = current_user).first()
            new_data = Master(payload['title'], payload['description'],
                              payload['qty'], payload['weight'],  payload['sku'],   payload['price'], payload['cost_price'],  payload['type'], payload['tags'] ,  payload['hsn'] , json.dumps(payload['variants']))
            user.masters.append(new_data)
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
@jwt_required
def get_master():
    schema = MasterSchema(many=True)
    current_user = get_jwt_identity()
    user = User.query.filter_by( username = current_user).first().masters
    return jsonify(schema.dump(user))


# Flow -> Create Porduct with Base Details -> get Product ID -> UPdate Inventory Level ( cost , sku )-> Return adn Add to local database .
# 


