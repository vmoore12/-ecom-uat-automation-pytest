# Automated Tests E-Commerce Site


## Description

This is an Automated Testing framework for a demo e-commerce site using Selenium webdriver and Pytest framework. The site under test is created using WordPress, Woocommerce and the StoreFront theme. Example site for testing [demostore.supersqa.com](https://demostore.supersqa.com)


## Prerequisites to run the tests

- You must have the E-Commerce site running

- The site must be created with WordPress & WooCommerce

- The site must be using the "StoreFront" theme

## Set environment variables to run tests

There are variables required by the framework. Some of these value can be changed directly in the code instead of setting environment variables but setting the environment variables is the easiest option. To change values in the code change them [here](ecom_uat_automation_pytest/automation/src/configs/MainConfigs.py)

### Here are the variables that must be set (For Windows on CMD replace 'export' with 'set')

export BASE_URL=`your website url` 

export BROWSER=`browser type`   

export RESULTS_DIR=`$(pwd)/results`  

export DB_PORT_OVERRIDE=`your database port`  

export DB_HOST_OVERRIDE=`your database host`  

export DB_DATABASE_OVERRIDE=`your site's database/schema name`  

export DB_TABLE_PREFIX_OVERRIDE=`your site's tables prefix`

## Credentials (these should not be kept in source control like GitHub)

export WOO_KEY=`your woocommerce api key`  
export WOO_SECRET=`your woocommerce api secret`
export DB_USER=`your database user`
export DB_PASSWORD=`your database password`
