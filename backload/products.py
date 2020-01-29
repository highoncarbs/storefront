from app import app , request , jsonify
from app import db , shop , shopify

from model import Master, MasterSchema


@app.route('/add/product', methods=['POST'])
def add_product():
    payload = request.json
    for item in payload:
        new_product = shopify.Product()
        new_product.title = item['name']
        new_product.body_html = item['description']
        new_product.tags = item['tags']
        new_product.product_type = item['type']
        success = new_product.save()
        product = new_product 
        if success:
            product = shopify.Product.find(new_product.id)
            product.variants[0].price = item['price']
            product.variants[0].inventory_management = "shopify"
            product.variants[0].inventory_quantity = item['qty']
            product.variants[0].sku = item['sku']+'-1'
            product.variants[0].weight= item['weight']
            product.variants[0].taxable= True
          
            # inventory.country_code_of_origin = "IN"
            # inventory.harmonized_system_code = "621490"
            # inventory.cost = item['cost_price']
          
            product.save()
            return jsonify({'message' : 'Product Added'})
        else:
            new_product.errors
            product.errors
        

        #  Add HSN Code to Product with Inventory Item API by sending IDS
        # Pass
        # new_product.price = item['price']
        # new_product.cost_price = item['cost_price']
        
        # # 
        # new_product.description = item['qty']
