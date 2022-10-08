from app import app, request, jsonify, json, requests, get_jwt_identity, jwt_required
from app import db

from model import Master, MasterSchema, Products, User, Orders, Item, OrdersSchema, OrdersMinSchema
from datetime import datetime, timedelta
import base64
import shopify

hours_added = timedelta(hours=6)


@app.route('/orders', methods=['GET'])
def ch_order():
    user = User.query.first()
    order_type = request.args['type']
    limit = request.args['show']

    if(user.shop_url != ""):
        if order_type == 'order':
            orders = requests.get(user.shop_url+'orders.json?status=any&limit='+limit)
            return orders.content
        else:
            orders = requests.get(user.shop_url+'checkouts.json')
            return orders.content

    return "{}", 501


@app.route('/orders/save', methods=['POST'])
def save_order():
    # user = User.query.first()
    # print(user)
    payload = request.json
    details = payload['details']
    curr_order = payload['order']
    last_inv_id = Orders.query.order_by(Orders.id.desc()).first()

    # Check if order exists with shopify order id
    chk_order = Orders.query.filter_by(
        shopify_order_id=curr_order['order_number']).first()
    # firm_inv_id = chk_order.firm_order_id

    if chk_order:
        firm_inv_id = chk_order.firm_order_id
    # if last_inv_id and not chk_order:
    #     firm_inv_id = int(last_inv_id.firm_order_id) + 1
    if details['inv_num']:
        firm_inv_id = details['inv_num']
    elif not chk_order:
        firm_inv_id = 1
    if not chk_order:
        order = Orders()
        for item in curr_order['line_items']:
            item_obj = Item(item['id'], item['product_id'], item['name'], item['quantity'], item['price'], getattr(
                item, 'tax', 0), getattr(item, 'tax', 0), getattr(item, 'discount', 0))
            order.item.append(item_obj)
    else:
        order = chk_order
        items = order.item
        for row in items:
            for item in curr_order['line_items']:
                if str(row.product_id) == str(item['id']):
                    row.tax = item['tax']
                    if 'discount' in item:
                        row.discount = int(item['discount'])
                    db.session.commit()
                # item_obj = Item(item['id'],item['product_id'],item['name'],item['quantity'],item['price'],item['tax'],item['discount'],0)
                # order.item.append(item_obj)

    order.shopify_order_id = curr_order['order_number']
    order.firm_order_id = firm_inv_id
    order.shipping_rate = details['shipping_rate']
    order.shipping_tax = details['shipping_tax']
    order.order_type = details['type']
    if details['gst'] != None:
        order.customer_gst = details.get('gst') if len(details.get('gst')) != 0 else ''
    else:
        order.customer_gst = ''
    order.inv_date = datetime.strptime(
        details['date'], '%Y-%m-%dT%H:%M:%S.%fZ') + hours_added
    order.customer_name = " ".join(
        (curr_order['customer']['first_name'], curr_order['customer']['last_name']))
    order.customer_address = json.dumps(
        curr_order['customer']['default_address'])
    order.shipping_address = json.dumps(curr_order['shipping_address'])
    order.customer_phone = curr_order['phone']
    order.customer_email = curr_order['contact_email']
    order.total_bill = curr_order['subtotal_price']
    if not chk_order:
        db.session.add(order)
    db.session.commit()
    # print(payload)
    return jsonify({'success': 'Order Saved'})


@app.route('/get/order/<id>', methods=['GET'])
def get_order(id):
    schema = OrdersSchema()
    order = Orders.query.filter_by(shopify_order_id=id).first()
    data = schema.dump(order)
    return data


@app.route('/get/order/inv/<id>', methods=['GET'])
def get_order_min(id):
    schema = OrdersMinSchema()
    order = Orders.query.filter_by(shopify_order_id=id).first()
    data = schema.dump(order)
    return data


@app.route('/product/<id>', methods=['GET'])
def get_prod_image(id):
    user = User.query.first()
    # print(user)
    if(user.shop_url != ""):
        orders = requests.get(user.shop_url+'/products/'+id+'/images.json')
        return orders.content
    return ""
