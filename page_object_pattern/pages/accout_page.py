import logging
import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.logout_button_class = 'c-button--narrow'
        self.my_data_link_text = 'Moje dane'
        self.orders_history_link_text = 'Historia zamówień'
        self.change_password_button_class = 'm-my-account-1__change-password'
        self.save_changes_button_class = 'js-save-account-data'
        self.name_input_name = 'name'
        self.surname_input_name = 'surname'
        self.email_input_name = 'email'
        self.phone_input_name = 'phone'
        self.street_input_name = 'street'
        self.home_num_input_name = 'home_number'
        self.postcode_input_name = 'postcode'
        self.city_input_name = 'city'
        self.address_addon_input_name = 'description'
        self.company_name_input_name = 'company_name'
        self.nip_input_name = 'company_nip'
        self.change_to_company_radio_button_class = 'c-radio-field__label'
        self.change_password_new_password_input_name = 'password'
        self.change_password_confirm_password_input_name = 'password_confirm'

    @allure.step('Logging out of account')
    def logout(self):
        self.logger.info('Clicking on logout button')
        self.driver.find_element_by_class_name(self.logout_button_class).click()
        allure.attach(self.driver.get_screenshot_as_png(), name='Products added to the basket', attachment_type=AttachmentType.PNG)

    @allure.step('Changing password')
    def change_password(self, password):
        self.driver.find_element_by_class_name(self.change_password_button_class).click()
        self.logger.info('Clicking on the "Change password" button')
        self.driver.find_element_by_name(self.change_password_new_password_input_name).send_keys(password)
        self.driver.find_element_by_name(self.change_password_confirm_password_input_name).send_keys(password)
        self.driver.find_element_by_name(self.change_password_confirm_password_input_name).send_keys(password+Keys.ENTER)







