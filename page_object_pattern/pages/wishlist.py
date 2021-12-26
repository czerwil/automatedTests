import time

import logging
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class WishlistPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.select_all_products_checkbox_class = 'm-wishlist-1__main-checkbox'
        self.delete_product_from_wishlist_class = 'js-remove-product-wishlist'
        self.add_selected_products_to_basket_button_class = 'js-add-selected-wishlist-product-to-cart'
        self.add_single_product_to_basket_button_class = 'js-add-wishlist-product-to-cart'
        self.product_title_class = 'c-table-product__title'
        self.basket_button_id = 'header-cart'
        self.cart_count_class = 'js-cart-count'
        self.cart_aside_product_title_class = 'c-aside-product__title'

    def get_product_title(self):
        product_title = self.driver.find_element_by_class_name(self.product_title_class).text
        return product_title

    def add_all_products_to_basket(self):
        self.logger.info("Selecting all products from wishlist")
        self.driver.find_element_by_class_name(self.select_all_products_checkbox_class).click()
        wishlist_count = len(self.driver.find_elements_by_class_name(self.product_title_class))
        self.logger.info("Adding {} products to cart".format(wishlist_count))
        self.driver.find_element_by_class_name(self.add_selected_products_to_basket_button_class).click()
        self.driver.find_element_by_id(self.basket_button_id).click()
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, self.cart_count_class)))
        cart_count = self.driver.find_element_by_class_name(self.cart_count_class).text
        product_name = self.driver.find_element_by_class_name(self.cart_aside_product_title_class).text
        self.logger.info("There are {} products in cart: {}".format(cart_count,product_name))
        return cart_count, product_name
