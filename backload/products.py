from app import app, request, jsonify, json, requests
from app import db, shop, shopify, SHOP_URL

from model import Master, MasterSchema, Products

import base64

from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


@app.route('/add/product', methods=['POST'])
def add_product():

    for idx, item_data in enumerate(request.form):
        item = json.loads(request.form[item_data])
        new_product = shopify.Product()
        new_product.title = item['name']
        new_product.body_html = item['description']
        new_product.tags = item['tags']
        new_product.product_type = item['type']
        new_product.metafields_global_title_tag = item['name']
        new_product.metafields_global_description_tag= strip_tags(item['description'])
        product = new_product
        image_payload = {}
        new_product.images = []
        # for file in request.files['files_' + str(idx) + '_0']:
        print(request.files)

        if len(request.files) != 0:
        # Image 1
            image_payload = {}
            file = request.files['files_0_0']   
            filename = file.filename
            temp = base64.b64encode(request.files['files_'+str(idx)+'_0'].read())
            temp = temp.decode("utf-8")
            image_payload['attachment'] = str(temp)
            image_payload['filename'] = str(filename)
            image_payload['position'] = int(1)
            image_payload['alt'] = str(filename).split('.')[0].replace('-', ' ')
            new_product.images.append(image_payload)
            # Image 2
            file = request.files['files_0_1']
            filename = file.filename
            image_payload = {}
            temp = base64.b64encode(request.files['files_'+str(idx)+'_1'].read())
            temp = temp.decode("utf-8")
            image_payload['attachment'] = str(temp)
            image_payload['filename'] = str(filename)
            image_payload['position'] = int(2)
            image_payload['alt'] = str(filename).split('.')[0].replace('-', ' ')
            
            new_product.images.append(image_payload)
        success = new_product.save()
        print(success, new_product.images)
       

        try:
            new_data = Products(product.id)
            if success:
                db.session.add(new_data)
                db.session.commit()
                product = shopify.Product.find(new_product.id)
                product.variants[0].price = item['price']
                product.variants[0].inventory_management = "shopify"
                product.variants[0].inventory_quantity = item['qty']
                product.variants[0].sku = item['sku']+str(new_data.id)
                product.variants[0].weight = item['weight']
                product.variants[0].taxable = False
                
                print(product.variants[0])
                # product.variants[0].harmonized_system_code = str(item['hsn'])
                new_data.sku = product.variants[0].sku
                product.save()
                db.session.commit()
                inventory_payload = {
                    "inventory_item": {
                        "id": str(product.variants[0].inventory_item_id),
                        "cost": str(item['cost_price']),
                        "country_code_of_origin": "IN",
                        "harmonized_system_code": str(item['hsn'])
                    }
                }
                print(inventory_payload)
                # image_payload = {}

                # for file in request.files['files_' + str(idx) + '[]']:
                #     filename = file.filename
                #     image_payload = {}
                #     temp = base64.b64encode(request.files['files_0_0'].read())
                #     image_payload['attachment'] = temp
                #     image_payload['filename'] = filename

                # # image_payloads = {'image':   image_payload}

                # # temp = base64.b64encode( request.files['files_0_1'].read())
                # # product.images.append({'attachment' : temp})

                headers = {"Content-Type": "application/json"
                           }
                inventory = requests.put(SHOP_URL + str('/inventory_items/{}.json').format(
                        product.variants[0].inventory_item_id), json=inventory_payload)

                print('Requests rsponse =---- ' , inventory.content)
                # try:
                #     image_url = requests.post(SHOP_URL + str('/products/{}/images.json').format(
                #         new_product.id), headers=headers, data=json.dump(image_payloads))
                # except Exception as e:
                #     print(image_url)
                #     print(str(e))

            else:
                print("New PRoduct errros")
                print(new_product.errors)
                print("Product Errors")
                print(product.errors)
        except Exception as e:
            print('Boom pa')
            print(str(e))

    return jsonify({'message': 'Product(s) Added'})
