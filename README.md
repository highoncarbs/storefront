
<p align="center">
<img align="left" src="./assets/header-0.png">
   <br><br>
</p>

Storefront to bulk manage for your shopify store

## Features 

 * Create Product Master Template 
 * Create and Edit Mulitple products at once , pre fill data from master template.  
 * View and Goto Products addded to Shopify
 * Generate Unique SKU's.

## In Progress Features

 * Upload Images  
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
