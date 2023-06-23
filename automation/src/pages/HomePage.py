
from src.selenium_extended.SeleniumExtended import SeleniumExtended
from src.configs.MainConfigs import MainConfigs
from src.pages.locators.HomePageLocators import HomePageLocators

class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def go_to_home_page(self):
        base_url = MainConfigs.get_base_url()
        self.driver.get(base_url)

    def click_first_add_to_cart_button(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BTN)

    def get_banner_text(self): 
       return self.sl.wait_and_get_text(self.FREE_SHIPPING_BANNER)
    

    def get_shop_heading(self): 
       return self.sl.wait_and_get_element(self.SHOP_HEADING)
    
    def get_all_products_name(self):
        return self.sl.wait_and_get_elements(self.ALL_PRODUCTS_NAMES)

