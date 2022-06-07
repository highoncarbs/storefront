from app import app, request, jsonify, json, requests, get_jwt_identity, jwt_required
from app import db

from model import Master, MasterSchema, Products, User
import json
import base64
import shopify
from html.parser import HTMLParser


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


@app.route('/check/add', methods=['GET'])
def chk_product():
    user = User.query.first()
    shopify.ShopifyResource.set_site(user.shop_url)
    shop = shopify.Shop.current()
    # product = shopify.Product.find(6570354737233)
    # print(product)
    # print(product.variants)
    # print(product.variants[0].inventory_item_id)
    # payload = {
    #     'inventory_item_id': product.variants[0].inventory_item_id,
    #     'available': 1500,
    #     'location_id': 34590130257,
    # }

    # inv_payload = {
    #     "inventory_item": {
    #         "id": product.variants[0].inventory_item_id,
    #         "tracked": True,
    #         "sku": 'TEst-sku',
    #         "country_code_of_origin": 'IN',
    #         "harmonized_system_code": 123456,

    #     }
    # }
    # inv_js_data = json.dumps(inv_payload)
    locs = requests.get(user.shop_url+'locations.json')
    print('location - - ', locs)
    print(locs.content)
    # url_path = user.shop_url+'inventory_items/' + \
    #     str(product.variants[0].inventory_item_id)+'.json?debug=true'
    # print('___S_S_', url_path)
    # inv_upd = requests.put(url_path, json=inv_payload)
    # # print(inv_upd.body/)/
    # print(inv_upd.content)
    # upd = requests.post(user.shop_url+'inventory_levels/set.json', payload)
    # print(upd.content)
    # print(shopify.Inventory.find(product.variants[0].inventory_item_id))
    # print()
    return "oj"


@app.route('/add/product', methods=['POST'])
# @jwt_required
def add_product():
    # current_user = get_jwt_identity()
    print('booom')
    user = User.query.first()
    print(user)
    if(user.shop_url != ""):

        for idx, item_data in enumerate(request.form):
            shopify.ShopifyResource.set_site(user.shop_url)
            shop = shopify.Shop.current()
            print(idx, 'ITEM UPLOADING')
            item = json.loads(request.form[item_data])
            new_product = shopify.Product()

            new_product.title = item['name']
            new_product.body_html = item['description']
            new_product.tags = item['tags']
            new_product.product_type = item['type']
            new_product.metafields_global_title_tag = item['name']
            new_product.metafields_global_description_tag = strip_tags(
                item['description'])
            product = new_product

            # print('hrer -- ',item)

            image_payload = {}
            new_product.images = []
            # for file in request.files:
            #     print(file)
            # print( idx , request.files['files_'+str(idx)])
            if len(request.files) != 0:
                # Image 1
                image_payload = {}
                try:
                    file = request.files['files_'+str(idx)+'_0']
                    filename = file.filename
                    temp = base64.b64encode(
                        request.files['files_'+str(idx)+'_0'].read())
                    temp = temp.decode("utf-8")
                    image_payload['attachment'] = str(temp)
                    image_payload['filename'] = str(filename)
                    image_payload['position'] = int(1)
                    image_payload['alt'] = str(filename).split('.')[
                        0].replace('-', ' ')
                    new_product.images.append(image_payload)
                except Exception as e:
                    pass
                # Image 2
                try:
                    file = request.files['files_'+str(idx)+'_1']
                    filename = file.filename
                    image_payload = {}
                    temp = base64.b64encode(
                        request.files['files_'+str(idx)+'_1'].read())
                    temp = temp.decode("utf-8")
                    image_payload['attachment'] = str(temp)
                    image_payload['filename'] = str(filename)
                    image_payload['position'] = int(2)
                    image_payload['alt'] = str(filename).split('.')[
                        0].replace('-', ' ')
                    new_product.images.append(image_payload)
                except Exception as e:
                    pass
                # Image 3
                try:
                    file = request.files['files_'+str(idx)+'_2']
                    filename = file.filename
                    image_payload = {}
                    temp = base64.b64encode(
                        request.files['files_'+str(idx)+'_2'].read())
                    temp = temp.decode("utf-8")
                    image_payload['attachment'] = str(temp)
                    image_payload['filename'] = str(filename)
                    image_payload['position'] = int(3)
                    image_payload['alt'] = str(filename).split('.')[
                        0].replace('-', ' ')
                    new_product.images.append(image_payload)
                except Exception as e:
                    pass
                # Image 4
                try:
                    file = request.files['files_'+str(idx)+'_3']
                    filename = file.filename
                    image_payload = {}
                    temp = base64.b64encode(
                        request.files['files_'+str(idx)+'_3'].read())
                    temp = temp.decode("utf-8")
                    image_payload['attachment'] = str(temp)
                    image_payload['filename'] = str(filename)
                    image_payload['position'] = int(4)
                    image_payload['alt'] = str(filename).split('.')[
                        0].replace('-', ' ')
                    new_product.images.append(image_payload)
                except Exception as e:
                    pass

            try:
                success = new_product.save()
            except Exception as e:
                print(str(e))
            # If no variants , do not run the below Inventory
            try:
                if success:
                    # For local pproduct storage
                    new_data = Products(product.id)
                    db.session.add(new_data)
                    db.session.commit()

                    product = shopify.Product.find(new_product.id)

                    price_payload = {
                        "variant":{
                            "id": product.variants[0].id,
                            "price": item['price'] ,
                            "weight": item['weight'] ,
                        }
                    }
                    qty_payload = {
                        'inventory_item_id': product.variants[0].inventory_item_id,
                        'available': item['qty'],
                        'location_id': 37804605579  # set up in settings,
                    }

                    inv_payload = {
                        "inventory_item": {
                            "id": product.variants[0].inventory_item_id,
                            "tracked": True,
                            "sku": str(item['sku']),
                            "country_code_of_origin": "IN",  # set in settings,
                            "harmonized_system_code": str(item['hsn']),

                        }
                    }

                    url_path = user.shop_url+'inventory_items/' + \
                        str(product.variants[0].inventory_item_id) + \
                        '.json?debug=true'
                    try:
                        inv_update_req = requests.put(url_path, json=inv_payload)
                        # print(inv_update_req)
                    except Exception as e:
                        print(str(e))
                    try:
                        qty_set_req = requests.post(user.shop_url+'inventory_levels/set.json?debug=true', qty_payload)
                        # print(qty_set_req)
                    except Exception as e:
                        print(str(e))
                    try:
                        var_price_req = requests.put(user.shop_url+'variants/'+str(product.variants[0].id)+'.json', json=price_payload)
                        # print(var_price_req)
                    except Exception as e:
                        print(str(e))


                    # product.variants[0].price = item['price']

            # After crearing product, get its variant from that get the inventory_item_id ,
            # from that update inventory ,
            #  set cost & hsn -"harmonized_system_code" in inventory item api & set "tracked": true
                # if success:
                #     db.session.add(new_data)
                #     db.session.commit()
                #     product = shopify.Product.find(new_product.id)
                #     if(len(item['variants']) != 0):
                #         product.variants[0].option1 = 'Swatch'
                #     product.variants[0].price = item['price']
                #     product.variants[0].inventory_management = "shopify"
                #     product.variants[0].inventory_quantity = item['qty']
                #     product.variants[0].sku = item['sku']+str(new_data.id)
                #     product.variants[0].weight = item['weight']
                #     product.variants[0].taxable = False

                # product.save()
                # # Create Product ID first
                # for (index_var, item_var) in enumerate(item['variants']):
                #     try:
                #         variant = {
                #             "option1": item_var['option'],
                #             "price": item_var['price'],
                #             "sku": item['sku']+item_var['option'],
                #             "weight": item['weight'],
                #             "taxable": False,
                #             "inventory_quantity": item_var['qty']
                #         }

                #         variant = requests.post(user.shop_url + str('/products/{}/variants.json').format(
                #             product.id), json={'variant': variant})

                #     except Exception as e:
                #         print(index_var, item_var, str(e))
                #         return jsonify({'messafe': 'Error uploading Products'})

                # db.session.commit()
                print('Uploaded Item - ', idx)

                # Updates Inventory for Base Item
                # inventory_payload = {
                #     "inventory_item": {
                #         "id": str(product.variants[0].inventory_item_id),
                #         "cost": str(item['cost_price']),
                #         "country_code_of_origin": "IN",
                #         "harmonized_system_code": str(item['hsn'])
                #     }
                # }

            except Exception as e:
                print('Boom pa')
                print(str(e))

        return jsonify({'success': 'Product(s) Added'})
    else:

        return jsonify({'message': 'SHOP URL not defined . Add one in settings'})
