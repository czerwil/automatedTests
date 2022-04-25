import logging
import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.cart_sum_value_class = 'js-cart-sum-value'
        self.cart_delivery_value_class = 'js-cart-delivery-value'
        self.cart_discount_value_class = 'at-cart-discount-value'
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
        self.cart_city_input_name = 'city'
        self.phone_input_name = 'phone'
        self.email_input_name = 'email'
        self.rules_acceptation_checkbox_class = 'c-checkbox-field__checkbox-container'
        self.cart_product_variants_class = 'c-table-product__variant'
        self.cart_login_form_inputs = 'at-login-form-input'
        self.cart_login_submit = 'at-login-form-submit'
        self.cart_delete_product_class_desktop = 'at-cart-product-delete-desktop'
        self.cart_login_form_email_input = 'at-login-form-input-email'
        self.cart_login_form_password_input = 'at-login-form-input-password'
        self.cart_discount_code_correct_message_class = 'm-cart-summary-box-1__discount-message--success'
        self.cart_discount_code_error_message_class = 'm-cart-summary-box-1__discount-message--fail'
        self.cart_inpost_map_search_input_id = 'easypack-search'
        self.cart_inpost_map_search_button_class = 'btn-search'
        self.cart_inpost_map_select_class = 'select-link'
        self.cart_inpost_map_locker_address_class = 'mobile-details-content'
        self.cart_shipment_inpost_locker_details_class = 'inpost_chosen'
        self.cart_inpost_map_search_list_class = 'inpost-search__item-list'
        self.cart_empty_cart_header_class = 'm-cart-empty-1__headline'
        self.cart_back_to_store_link_text = 'Wróć do sklepu'

    @allure.step('Getting single product data from basket')
    def get_product_data(self):
        wait = WebDriverWait(self.driver, 3)
        name = self.driver.find_element_by_class_name(self.cart_product_title_class).text
        quantity = self.driver.find_element_by_class_name(self.cart_product_quantity_input_class).get_attribute('value')
        try:
            wait.until(expected_conditions.visibility_of_element_located(
                (By.CLASS_NAME, self.cart_product_price_after_discount_class)))
            price = self.driver.find_element_by_class_name(self.cart_product_price_after_discount_class).text
        except:
            price = self.driver.find_element_by_class_name(self.cart_product_price_original_class).text
        # try:
        #     available_variants = self.driver.find_elements_by_class_name(self.cart_product_variants_class)
        #     variants = []
        #     for variant in available_variants:
        #         variants.append(variant.text)
        # except:
        #        pass
        # Nie jesteśmy na to jeszcze gotowi, bo z wyciągą nazwę wariantu łącznie z jego cechą
        return name, price, quantity

    @allure.step('Setting passed delivery method')
    def set_delivery_method(self, delivery='test'):
        delivery_methods = self.driver.find_elements_by_class_name(self.cart_shipment_name_class)
        delivery_methods_names = []
        for method in delivery_methods:
            delivery_methods_names.append(method.text)
            time.sleep(0.3)
        self.logger.info("There are {} available delivery methods:".format(len(delivery_methods)))
        for i in range(len(delivery_methods)):
            self.logger.info('{}'.format(delivery_methods_names[i]))
        for method in delivery_methods:
            time.sleep(0.2)
            if method.text == delivery:
                self.logger.info("Setting delivery method to {}".format(method.text))
                method.click()
        allure.attach(self.driver.get_screenshot_as_png(), name='delivery method has been set',
                      attachment_type=AttachmentType.PNG)

    @allure.step('Setting passed payment method')
    def set_payment_method(self, payment='test'):
        payment_methods = self.driver.find_elements_by_class_name(self.cart_payment_name_class)
        payment_methods_names = []
        for method in payment_methods:
            payment_methods_names.append(method.text)
            time.sleep(0.3)
        self.logger.info("There are {} available payment methods".format(len(payment_methods)))
        for i in range(len(payment_methods)):
            self.logger.info('{}'.format(payment_methods_names[i]))
        for method in payment_methods:
            if method.text == payment:
                self.logger.info("Setting payment method to {}".format(method.text))
                method.click()
        allure.attach(self.driver.get_screenshot_as_png(), name='payment method has been set',
                      attachment_type=AttachmentType.PNG)
        return payment_methods_names

    @allure.step('Using discount code inside checkout and returns reply message')
    def use_discount_code(self, code):
        wait = WebDriverWait(self.driver, 2)
        self.driver.find_element_by_class_name(self.cart_discount_code_label).click()
        self.logger.info("Using discount code: {}".format(code))
        self.driver.find_element_by_class_name(self.cart_discount_code_input_class).send_keys(code)
        try:
            wait.until(expected_conditions.visibility_of_element_located(
                (By.CLASS_NAME, self.cart_discount_code_correct_message_class)))
            message = self.driver.find_element_by_class_name(self.cart_discount_code_correct_message_class).text
        except:
            wait.until(expected_conditions.visibility_of_element_located(
                (By.CLASS_NAME, self.cart_discount_code_error_message_class)))
            message = self.driver.find_element_by_class_name(self.cart_discount_code_error_message_class).text
        self.logger.info('Getting discount message: {}'.format(message))
        allure.attach(self.driver.get_screenshot_as_png(), name='discount code has been applied to the cart',
                      attachment_type=AttachmentType.PNG)
        return message

    @allure.step('Going to next checkout step')
    def next_step(self):
        self.driver.find_element_by_class_name(self.cart_next_button_class).click()
        time.sleep(1)
        allure.attach(self.driver.get_screenshot_as_png(), name='next checkout step',
                      attachment_type=AttachmentType.PNG)
        return self.driver.current_url

    @allure.step('Completing delivery data inside checkout')
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
        allure.attach(self.driver.get_screenshot_as_png(), name='delivery data has been send',
                      attachment_type=AttachmentType.PNG)

    @allure.step('Checking if the summary is correct, returns True/False')
    def check_summary_correctness(self):
        sum = self.driver.find_element_by_class_name(self.cart_sum_value_class).text
        sum = float(sum.replace(',', '.'))
        discount = self.driver.find_element_by_class_name(self.cart_discount_value_class).text
        discount = float(discount.replace(',', '.'))
        delivery = self.driver.find_element_by_class_name(self.cart_delivery_value_class).text
        delivery = float(delivery.replace(',', '.'))
        overall = self.driver.find_element_by_class_name(self.cart_overall_value_class).text
        overall = float(overall.replace(',', '.'))
        return sum - discount + delivery == overall

    @allure.step('Logging in inside the checkout page')
    def login_inside_checkout(self, credentials):
        self.driver.find_element_by_class_name(self.cart_login_form_email_input).send_keys(credentials[0])
        self.driver.find_element_by_class_name(self.cart_login_form_password_input).send_keys(credentials[1])
        self.driver.find_element_by_class_name(self.cart_login_submit).click()
        allure.attach(self.driver.get_screenshot_as_png(), name='logging in', attachment_type=AttachmentType.PNG)
        time.sleep(2)

    @allure.step('Removing single product from cart')
    def remove_product_from_the_cart(self):
        self.logger.info("Removing product from the cart")
        self.driver.find_element_by_class_name(self.cart_delete_product_class_desktop).click()
        time.sleep(0.5)
        allure.attach(self.driver.get_screenshot_as_png(), name='removing product from the cart',
                      attachment_type=AttachmentType.PNG)

    @allure.step('Setting parcel locker (Paczkomat)')
    def set_parcel_locker(self, locker_name):
        wait = WebDriverWait(self.driver, 5)
        self.driver.find_element_by_id(self.cart_inpost_map_search_input_id).send_keys(locker_name)
        wait.until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, self.cart_inpost_map_search_list_class)))
        self.driver.find_element_by_class_name(self.cart_inpost_map_search_button_class).click()
        self.logger.info("Searching for parcel locker: {}".format(locker_name))
        wait.until(expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, self.cart_inpost_map_locker_address_class)))
        locker_address = self.driver.find_element_by_class_name(self.cart_inpost_map_locker_address_class).text
        self.logger.info("Address of the selected locker is: {}".format(locker_address))
        allure.attach(self.driver.get_screenshot_as_png(), name='selecting the parcel locker',
                      attachment_type=AttachmentType.PNG)
        self.driver.find_element_by_class_name(self.cart_inpost_map_select_class).click()
        self.logger.info("Locker has been selected".format(locker_address))
        locker_address_checkout = self.driver.find_element_by_class_name(
            self.cart_shipment_inpost_locker_details_class).text
        locker_address = locker_address.replace('\n', ', ')
        return locker_address, locker_address_checkout

    @allure.step('Checking that basket is empty and redirecting to the store homepage')
    def check_that_basket_is_empty(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, self.cart_empty_cart_header_class)))
        header = self.driver.find_element_by_class_name(self.cart_empty_cart_header_class).text
        self.logger.info('{}'.format(header))
        self.logger.info("Redirecting to the store homepage")
        allure.attach(self.driver.get_screenshot_as_png(), name='Empty basket', attachment_type=AttachmentType.PNG)
        self.driver.find_element_by_link_text(self.cart_back_to_store_link_text).click()
        if header == 'Twój koszyk jest pusty':
            return True
