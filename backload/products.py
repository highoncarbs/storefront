from app import app, request, jsonify, json, requests
from app import db, shop, shopify, SHOP_URL

from model import Master, MasterSchema, Products

import base64


@app.route('/add/product', methods=['POST'])
def add_product():

    for idx, item_data in enumerate(request.form):
        item = json.loads(request.form[item_data])
        new_product = shopify.Product()
        new_product.title = item['name']
        new_product.body_html = item['description']
        new_product.tags = item['tags']
        new_product.product_type = item['type']
        success = new_product.save()
        product = new_product
        product.images = []

        # Image Upload Needs work -

        # for file in request.files['files_' + str(idx) + '[]']:
        # temp = base64.b64encode( request.files['files_0_0'].read())
        # product.images.append({'attachment' : temp})
        # temp = base64.b64encode( request.files['files_0_1'].read())
        # product.images.append({'attachment' : temp})

        try:
            new_data = Products(product.id)
            db.session.add(new_data)
            db.session.commit()
            if success:
                product = shopify.Product.find(new_product.id)
                product.variants[0].price = item['price']
                product.variants[0].inventory_management = "shopify"
                product.variants[0].inventory_quantity = item['qty']
                product.variants[0].sku = item['sku']+str(new_data.id)
                product.variants[0].weight = item['weight']
                product.variants[0].taxable = True
                new_data.sku = product.variants[0].sku
                product.save()
                db.session.commit()
                print(item['hsn'])
                inventory_payload = {
                    "inventory_item": {
                        "id": product.variants[0].inventory_item_id,
                        "cost": item['cost_price'],
                        "country_code_of_origin": "IN",
                        "harmonized_system_code": item['hsn']
                    }
                }
                headers = {'content-type': 'application/json'}

                inventory = requests.put(SHOP_URL + str('/inventory_items/{}.json').format(
                    product.variants[0].inventory_item_id), headers=headers, data=json.dumps(inventory_payload))

            else:
                print(new_product.errors)
                print(product.errors)
        except Exception as e:
            print(str(e))

    return jsonify({'message': 'Product Added'})
