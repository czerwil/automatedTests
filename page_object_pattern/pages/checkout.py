import logging
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.cart_sum_value_class = 'js-cart-sum-value'
        self.cart_delivery_value_class = 'js-cart-delivery-value'
        self.cart_discount_value_class ='js-cart-discount-value'
        self.cart_overall_value_class = 'js-cart-sum-overal-value'
        self.cart_next_button_class = 'js-cart-next'
        self.cart_back_button_class = 'js-cart-back'
        self.cart_delete_item_class = 'js-cart-product-delete'
        self.cart_product_price_after_discount_class = 'at-cart-product-price-after-discount'
        self.cart_product_sum_value_after_discount_class = 'js-cart-price-after-discount-sum'
        self.cart_product_price_original_class = 'at-cart-product-price-original'
        self.cart_product_sum_value_original_class = 'js-cart-price-original-sum'
        self.cart_product_quantity_input_class = 'c-table-product__quantity-input'
        self.cart_discount_code_checkbox_class = 'at-cart-discount-checkbox'
        self.cart_discount_code_label = 'm-cart-summary-box-1__desktop-discount'
        self.cart_discount_code_input_class = 'js-cart-discount-input'
        self.cart_shipment_option_class = 'js-cart-shipment-option'
        self.cart_shipment_name_class = 'js-cart-shipment-name'
        self.cart_payment_option_class = 'js-cart-payment-option'
        self.cart_payment_name_class = 'js-cart-payment-name'
        self.cart_product_title_class = 'c-table-product__title'


    def get_product_data(self):
        name = self.driver.find_element_by_class_name(self.cart_product_title_class).text
        quantity = self.driver.find_element_by_class_name(self.cart_product_quantity_input_class).get_attribute('value')
        try:
            price = self.driver.find_element_by_class_name(self.cart_product_price_after_discount_class).text
        except:
            price = self.driver.find_element_by_class_name(self.cart_product_price_after_discount_class).text
        return name,price,quantity

    def set_delivery_method(self):
        delivery_methods = self.driver.find_elements_by_class_name(self.cart_shipment_name_class)
        self.logger.info("There are {} available delivery methods".format(len(delivery_methods)))
        for method in delivery_methods:
            method.click()
            self.logger.info("Setting delivery method to {}".format(method.text))
        return delivery_methods

    def set_payment_method(self):
        payment_methods = self.driver.find_elements_by_class_name(self.cart_payment_name_class)
        self.logger.info("There are {} available payment methods".format(len(payment_methods)))
        for method in payment_methods:
            method.click()
            self.logger.info("Setting payment method to {}".format(method.text))
        return payment_methods

    def use_discount_code(self, code):
        self.driver.find_element_by_class_name(self.cart_discount_code_label).click()
        self.logger.info("Using discount code {}".format(code))
        self.driver.find_element_by_class_name(self.cart_discount_code_input_class).send_keys(code)














