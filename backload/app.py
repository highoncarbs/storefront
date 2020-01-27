from model import Master, MasterSchema
import logging
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
CORS(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)


baseUrl = 'https://c5673965f8cef9f48d175bad834a39aa:ad4fd2c761999a71e58d3b22884cbef5@highoncarbs.myshopify.com/admin/api/2019-10/'


@app.route('/get/products', methods=['GET'])
def get_products():
    data = requests.get(baseUrl + str('products.json'))
    return data.json()


@app.route('/add/master', methods=['POST'])
def add_master():
    payload = request.json
    if payload is not None:
        try:
            new_data = Master(payload['name'], payload['description'], /
                              payload['qty'], payload['weight'],  payload['sku'],   payload['pricing'], payload['cost_price'],  payload['type'], payload['tags'])
            db.session.add(new_data)
            db.session.commit()
            return jsonify('success': 'Data Added')

        except IntegrityError as e:
            return jsonify('message': 'Duplicate Data')
        except Exception as e:
            return jsonify('message': 'Data Entry Error')
    return jsonify('message': 'Empty request')


@app.route('/view/master', methods=['POST'])
def view_master():
    schema = MasterSchema(many=True)
    data = Master.query.all()

    return jsonify(schema.dump(data))


if __name__ == "__main__":
    app.run(debug=True)
