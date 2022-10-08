# from flask import Blueprint
from flask import redirect, url_for, request, session, jsonify, current_app
# from app.basic_master import bp
from model import Fabric, FabricSchema
from app import db, ma
import app
import json


@app.route('/get/fabric', methods=['GET'])
def get_uom():

        data_schema = FabricSchema(many=True)
        data = Fabric.query.order_by(Fabric.name).all()
        json_data = data_schema.dump(data)
        return jsonify(json_data)


@app.route('/add/fabric', methods=['POST'])
def add_uom():
        payload = request.json
        if len(payload['name']) != 0:

            check_data = Fabric.query.filter_by(
                name=payload['name'].lower().strip())
            if check_data.first():
                return jsonify({'message': 'Data - '+check_data.first().name+' already exists.'})
            else:
                try:
                    new_data = Fabric(
                        payload['name'].lower().strip())

                    db.session.add(new_data)
                    db.session.commit()
                    json_data = {'id': new_data.id, 'name': new_data.name}
                    return jsonify({'success': 'Data Added', 'data': json_data})

                except Exception as e:
                    print(str(e))
                    db.session.rollback()
                    db.session.close()
                    return jsonify({'message': 'Something unexpected happened. Check logs', 'log': str(e)})
        else:
            return jsonify({'message': 'Empty Data.'})


@app.route('/edit/fabric', methods=['POST'])
def edit_uom():

        payload = request.json
        if payload['name'] is not None:

            check_data = Fabric.query.filter_by(
                name=payload['name'].lower().strip()).first()
            if check_data and check_data.name != payload['name'].lower().strip():
                return jsonify({'message': 'Data - '+check_data.name+' already exists.'})
            else:
                try:
                    new_data = Fabric.query.filter_by(
                        id=payload['id']).first()
                    new_data.name = payload['name'].lower().strip()
                    db.session.commit()
                    return jsonify({'success': 'Data Updated'})

                except Exception as e:
                    print(str(e))

                    db.session.rollback()
                    db.session.close()
                    return jsonify({'message': 'Something unexpected happened. Check logs', 'log': str(e)})
        else:
            return jsonify({'message': 'Empty Data.'})

 

@app.route('/delete/fabric', methods=['POST'])
def delete_uom():
        payload = request.json
        check_data = Fabric.query.filter_by(id=payload['id'])
        if check_data.first():
            if len(check_data.first().uom_category) is int(0) and len(check_data.first().uom_goods) is int(0) and len(check_data.first().uom_category_basic) is int(0) :

                try:
                    check_data.delete()
                    db.session.commit()
                    return jsonify({'success': 'Data deleted'})
                except Exception as e:
                    db.session.rollback()
                    db.session.close()
                    return jsonify({'message': 'Something unexpected happened. Check logs', 'log': str(e)})
            else:
                return jsonify({'message': 'Cannot delete data. Being used by other master.'})

        else:
            return jsonify({'message': 'Data does not exist.'})
