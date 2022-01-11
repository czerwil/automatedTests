import logging
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.cart_sum_value_class = 'js-cart-sum-value'
        self.cart_delivery_value_class = 'js-cart-delivery-value'
        self.cart_discount_value_class ='at-cart-discount-value'
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
        self.cart_name_input_name = 'name'
        self.cart_surname_input_name = 'surname'
        self.cart_street_input_name = 'street'
        self.cart_home_number_input_name = 'home_number'
        self.cart_postcode_input_name = 'postcode'
        self.cart_city_input_name ='city'
        self.phone_input_name = 'phone'
        self.email_input_name = 'email'
        self.rules_acceptation_checkbox_class = 'c-checkbox-field__checkbox-container'
        self.cart_product_variants_class = 'c-table-product__variant'
        self.cart_login_form_inputs = 'at-login-form-input'
        self.cart_login_submit = 'at-login-form-submit'
        self.cart_delete_product_class = 'at-cart-product-delete'


    def get_product_data(self):
        name = self.driver.find_element_by_class_name(self.cart_product_title_class).text
        quantity = self.driver.find_element_by_class_name(self.cart_product_quantity_input_class).get_attribute('value')
        try:
            price = self.driver.find_element_by_class_name(self.cart_product_price_after_discount_class).text
        except:
            price = self.driver.find_element_by_class_name(self.cart_product_price_after_discount_class).text
        try:
            available_variants = self.driver.find_elements_by_class_name(self.cart_product_variants_class)
            variants = []
            for variant in available_variants:
                variants.append(variant.text)
        except:
            pass
        return name,price,quantity,variants

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
        wait = WebDriverWait(self.driver,2)
        self.driver.find_element_by_class_name(self.cart_discount_code_label).click()
        self.logger.info("Using discount code {}".format(code))
        self.driver.find_element_by_class_name(self.cart_discount_code_input_class).send_keys(code)
        wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, self.cart_discount_value_class)))

    def next_step(self):
        self.driver.find_element_by_class_name(self.cart_next_button_class).click()
        time.sleep(1)

    def complete_delivery_data(self, delivery_data):
        self.logger.info('Completing delivery data')
        self.logger.info('Setting name to: {}'.format(delivery_data[0]))
        self.driver.find_element_by_name(self.cart_name_input_name).send_keys(delivery_data[0])
        self.logger.info('Setting surname to: {}'.format(delivery_data[1]))
        self.driver.find_element_by_name(self.cart_surname_input_name).send_keys(delivery_data[1])
        self.logger.info('Setting street to: {}'.format(delivery_data[2]))
        self.driver.find_element_by_name(self.cart_street_input_name).send_keys(delivery_data[2])
        self.logger.info('Setting name home number to: {}'.format(delivery_data[3]))
        self.driver.find_element_by_name(self.cart_home_number_input_name).send_keys(delivery_data[3])
        self.logger.info('Setting postcode to: {}'.format(delivery_data[4]))
        self.driver.find_element_by_name(self.cart_postcode_input_name).send_keys(delivery_data[4])
        self.logger.info('Setting city to: {}'.format(delivery_data[5]))
        self.driver.find_element_by_name(self.cart_city_input_name).send_keys(delivery_data[5])
        self.logger.info('Setting phone number to: {}'.format(delivery_data[6]))
        self.driver.find_element_by_name(self.phone_input_name).send_keys(delivery_data[6])
        self.logger.info('Setting email to: {}'.format(delivery_data[7]))
        self.driver.find_element_by_name(self.email_input_name).send_keys(delivery_data[7])
        self.driver.find_element_by_class_name(self.rules_acceptation_checkbox_class).click()

    def check_summary_correctness(self):
        sum = self.driver.find_element_by_class_name(self.cart_sum_value_class).text
        sum = float(sum.replace(',','.'))
        discount = self.driver.find_element_by_class_name(self.cart_discount_value_class).text
        discount = float(discount.replace(',','.'))
        delivery = self.driver.find_element_by_class_name(self.cart_delivery_value_class).text
        delivery = float(delivery.replace(',','.'))
        overall = self.driver.find_element_by_class_name(self.cart_overall_value_class).text
        overall = float(overall.replace(',','.'))
        return sum - discount + delivery == overall

    def login_inside_checkout(self, credentials):
        input_fields  = self.driver.find_elements_by_class_name(self.cart_login_form_inputs)
        i = 0
        for input in input_fields:
            input.send_keys(credentials[i])
            i = 1
        self.driver.find_element_by_class_name(self.cart_login_submit).click()
        time.sleep(2)

    def remove_products_from_the_cart(self):
        self.driver.find_element_by_class_name(self.cart_delete_product_class).click()




















