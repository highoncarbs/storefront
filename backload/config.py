# Config for automato 
# WTF config
class Config(object):

    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'the_very_secure_secret_security_key_that_no_will_ever_guess'

    # MySQL Config

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:alpine@127.0.0.1/storefront'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = './../uploads'

SHOP_URL = 'https://API_KEY:PASSWORD@store.myshopify.com/admin/api/2019-10/'
