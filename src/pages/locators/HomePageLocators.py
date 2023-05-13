from selenium.webdriver.common.by import By

class HomePageLocators:

    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'li.product a.button.add_to_cart_button')
    FREE_SHIPPING_BANNER = (By.CSS_SELECTOR, 'td div.wpfront-message.wpfront-div strong')
    SHOP_HEADING = (By.CSS_SELECTOR, 'div.content-area header.woocommerce-products-header h1')
    ALL_PRODUCTS_NAMES = (By.CSS_SELECTOR, '.products li.type-product .woocommerce-loop-product__title')