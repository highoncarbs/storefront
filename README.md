
<p align="center">
<h2 align="center"> Storefront helps bulk manage and upload products to your shopify store </h2>
   <br>
<img align="center" src="./assets/header-0.png">
</p>

## 📝 Quicknote

This is a very hacky project to bulk upload to shopify . Supports all the Basic features - but has a few knacks here and there -

 * Error Reporting not implmented 
 * HSN codes should be accurate - else would not be added 
 * 2 Images should be uploaded for each product to make image uploading work ( can be changed and updated as you like in the code) 
 * Meta title and description picked up from the title and body of the product   
 * You shop URI should be added to the config, the settings SHOP URL doesn't work for now.

Feel free to submit issues , if you get stuck somewhere . Would be more than happy to help . Cheers !   

## Features 

 * Create Product Master Template 
 * Create and Edit Mulitple products at once , pre fill data from master template.  
 * View and Goto Products addded to Shopify
 * Generate Unique SKU's.
 * Adds ALT tag text to the image
 * Upload Images - Fixed to 2 ( Requires to add 2 images to work or else ti would throw error)   

## In Progress Features

 * Analytics  
 * Print SKU Product Stickers
 * View orders and print shipping lables and invoices


## Build Setup

``` bash
# install dependencies
$ npm run install

# serve with hot reload at localhost:3000
$ npm run dev

# build for production and launch server
$ npm run build
$ npm run start

```

## Edit config.py 

Storefront requires access to your Shopify store via a Private App URL

``` bash
# Set SHOP_URl in config.py 
SHOP_URL = 'https://API_KEY:PASSWORD@store.myshopify.com/admin/api/2019-10/'

```

## Run Python Backend

``` bash
# install dependencies
$ pip install -r requirements.txt

# serve with hot reload at localhost:5000
$ python run.py


```


## Made With
 * Nuxtjs
 * Bulma & Buefy  
 * Flask
 * SQLAlcehmy.
 * Flask-migrate.
 * Shopify.
