# Config for automato 
# WTF config
class Config(object):

    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'the_very_secure_secret_security_key_that_no_will_ever_guess'

    # MySQL Config

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:alpine@127.0.0.1/storefront'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_BLACKLIST_ENABLED = True
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

UPLOAD_FOLDER = './../storefront/static/uploads'
SHOP_URL = 'https://1d7033901e1b0aca6932958286ab63d9:347218000a14c6b69b71d1c69e2536f5@itminan.myshopify.com/admin/api/2020-01/'
