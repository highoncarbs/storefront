from flask import redirect, url_for, request, session , jsonify , current_app
from model import User , UserSchema
# from app.auth.forms import LoginForm, RegistrationForm
# from app.model import UserSchema
from app import app, db, jwt
from config import UPLOAD_FOLDER
from flask_jwt_extended import jwt_required, get_jwt_identity,create_access_token, create_refresh_token,jwt_refresh_token_required, get_raw_jwt
import datetime
import json        
import os 
blacklist = set()
UPLOAD_FOLDER = os.path.abspath(UPLOAD_FOLDER)

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist

@app.route('/login',  methods=[ 'POST'])
def login():
    auth = request.json
    if auth:
        user = User.query.filter(User.username == str(auth['username']).lower()).first()
        if user:
            if( user.check_password(auth['password'])):
                access_token = create_access_token(identity=auth['username'])
                refresh_token = create_refresh_token(identity=auth['username'])
                return jsonify({'token': access_token , 'refresh_token': refresh_token})
            else:
                return jsonify({'message': "Invalid Data"})
        else:
            return jsonify({'message': "Invalid Data"})
    else:
        return jsonify({'message': "Invalid Data"})

@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'token': create_access_token(identity=current_user)
    }
    return jsonify(ret), 200

@app.route('/user', methods=['GET'])
@jwt_required
def get_user_details():
    current_user = get_jwt_identity()
    user_role = User.query.filter(User.username == current_user).first()
    return jsonify({'user': { 'name':current_user, 'shop_url': user_role.shop_url,'shop_name': user_role.shop_name, 'id' : user_role.id} })

@app.route('/get/user/firm', methods=['GET'])
@jwt_required
def get_user_firm():
    current_user = get_jwt_identity()
    user_firm = User.query.filter(User.username == current_user).first()
    schema = UserSchema()
    data = schema.dump(user_firm)
    return jsonify(data)
    return jsonify({'user': { 'name':current_user, 'shop_url': user_role.shop_url,'shop_name': user_role.shop_name, 'id' : user_role.id} })

# TODO Handel if invalid or dumplicate username & passowrd when editing user -!

@app.route('/update/user/firm', methods=['POST'])
@jwt_required
def update_user_details():
    payload = json.loads(request.form['data'])
    firm_logo = request.files
    print(firm_logo)
    current_user = get_jwt_identity()
    user = User.query.filter(User.username == current_user ).first()
    if (user.shop_url != ""):

            user.firm_name = payload['firm']['name']
            user.firm_phone = payload['firm']['phone']
            user.firm_gst = payload['firm']['gst']
            user.firm_address = payload['firm']['address']
            user.order_start = payload['firm']['order_start']
            db.session.commit()
    if len(firm_logo) != 0:
        for sub_index,img in enumerate(firm_logo.items()):
            try:
                print(img)
                file = img[1]
                print('~~', file)
                if file:
                    if os.path.exists(UPLOAD_FOLDER):
                        filetemp = os.path.join(
                            UPLOAD_FOLDER, file.filename)
                        file.save(filetemp)
                        user.image = file.filename
                        print(file.filename)
                        db.session.commit()
                    else:

                        os.makedirs(UPLOAD_FOLDER)

                        filetemp = os.path.join(
                            UPLOAD_FOLDER, file.filename)
                        file.save(filetemp)
                        user.image = file.filename
                        db.session.commit()
                else:
                    return jsonify({'message': 'Image file not supported.'})

            except KeyError as e:
                print(str('ERROR adding image and saving to local disk',file,e))
                return jsonify({'message': 'Error saving image - '+file,'log':str(e)})

            except Exception as e:
                print(str(e))

        # db.session.commit()
        return jsonify({'success': 'Firm Updated'}) , 200
    return jsonify({'message': "Empty Shop URL" , 'error' : 'shop_url' })

@app.route('/update/user', methods=['POST'])
@jwt_required
def update_user_firm():
    payload = request.json
    current_user = get_jwt_identity()
    user = User.query.filter(User.username == current_user ).first()
    if (payload['shop_url'] != ""):
        
            user.shop_url = payload['shop_url']
            user.shop_name = payload['shop_name']
            db.session.commit()
            return jsonify({'success': 'Shop Updated'}) , 200
  
    return jsonify({'message': "Empty Shop URL" , 'error' : 'shop_url' })

# @app.route('/userlist', methods=['GET'])
# @jwt_required
# def get_user_list():
#     current_user = get_jwt_identity()
#     users = User.query.all()
#     # schema = UserSchema(many=True)
#     data = schema.dump(users)
    
#     return jsonify(data)

@app.route('/create',  methods=['POST'])
def create_user():
    payload = request.json
    user = str(payload['username']).lower()
    password = payload['password']
    check_user = User.query.filter(User.username == user)
    try:
        if not check_user.first():
            new_user = User(user)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'success': "User Created"})
        else:
            return jsonify({'message': "Username already exists" , 'error': 'username'})
    except Exception as e:
        print(str(e))
        return jsonify({'message': "Unable to Create User"})
        
        

@app.route('/logout', methods=['DELETE'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify({"message": "Successfully logged out"}), 200