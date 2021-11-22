import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class WishlistPage:

    def __init__(self, driver):
        self.driver = driver
        #self.logger =
        self.check_all_products_checkbox_class = 'm-wishlist-1__main-checkbox'
        self.delete_product_from_wishlist_class = 'js-remove-product-wishlist'
        self.add_selected_products_to_basket_button_class = 'js-add-selected-wishlist-product-to-cart'
        self.add_single_product_to_basket_button_class = 'js-add-wishlist-product-to-cart'
        self.product_title_class = 'c-table-product__title'

    def get_product_title(self):
        product_title = self.driver.find_element_by_class_name(self.product_title_class).text
        return product_title

