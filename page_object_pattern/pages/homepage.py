import time

import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.header_logo_class = 'm-header-1__logo-link'
        self.search_query_id = 'header_search_query'
        self.contact_call_class = 'm-header-1__contact-call'
        self.contact_form_button_class = 'm-header-1__contact-button'
        self.account_button_id = 'header-account'
        self.wishlist_button_id = 'header-wishlist'
        self.cart_button_id = 'header-cart'
        self.newsletter_email_input_class = 'js-newsletter-source-input'
        self.newsletter_submit_button_class = 'js-newsletter-trigger'
        self.news_container_class = 'm-news-panel-1__box'
        self.cookie_popup_accept_button_class = 'js-accept-cookie-alert-1'
        self.newsletter_alert_span_xpath = '//*[@id="modal-aside-newsletter"]/div[2]/div[2]/div/form/label/span'
        #Dodać klasy inputów z danymi do logowania/rejestracji
        self.login_form_email_input_name = 'email'
        self.login_form_password_input_name = 'password'
        self.login_form_confirm_password_input_name = 'password_confirm'
        self.register_form_terms_of_condition_checkbox_label_class = 'c-checkbox-field__label'
        self.regist = 'at-aside-register-input'
        self.switch_to_register_form_class = 'js-modal-aside-register'
        self.login_confirm_button_class = 'js-submit-login'
        self.my_account_link_text = 'Moje dane'
        self.newsletter_pop_up_class = 'l-popup__message'
        self.newsletter_pop_up_text_class = 'l-popup__message-content'




    def perform_search(self,query):
        self.driver.find_element_by_id(self.search_query_id).click()
        self.driver.find_element_by_id(self.search_query_id).send_keys(query + Keys.ENTER)

    def accept_cookie_policy(self):
        self.driver.find_element_by_class_name(self.cookie_popup_accept_button_class).click()

    def subscribe_to_newsletter_fail(self, email):
        self.logger.info("Subscribing for newsletter:")
        self.logger.info("Sending email address{}".format(email))
        self.driver.find_element_by_class_name(self.newsletter_email_input_class).send_keys(email)
        self.logger.info("Clicking subscribe button")
        self.driver.find_element_by_class_name(self.newsletter_submit_button_class).click()
        time.sleep(1)
        alert = self.driver.find_element_by_xpath(self.newsletter_alert_span_xpath)
        self.logger.info("Got alert message: {}".format(alert.text))
        return alert

    def subscribe_to_newsletter_success(self, email):
        wait = WebDriverWait(self.driver,3)
        self.logger.info("Subscribing for newsletter:")
        self.logger.info("Sending email address{}".format(email))
        self.driver.find_element_by_class_name(self.newsletter_email_input_class).send_keys(email)
        self.logger.info("Clicking subscribe button")
        self.driver.find_element_by_class_name(self.newsletter_submit_button_class).click()
        wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,self.newsletter_pop_up_class)))
        pop_up_text = self.driver.find_element_by_class_name(self.newsletter_pop_up_text_class).text
        self.logger.info("Got message: {}".format(pop_up_text))
        return pop_up_text


    def register_account(self, email, password):
        self.driver.find_element_by_id(self.account_button_id).click()
        self.driver.find_element_by_class_name(self.switch_to_register_form_class).click()
        self.driver.find_element_by_name(self.login_form_email_input_name).send_keys(email)
        self.driver.find_element_by_name(self.login_form_password_input_name).send_keys(password)
        self.driver.find_element_by_name(self.login_form_confirm_password_input_name).send_keys(password)
        self.driver.find_element_by_class_name(self.register_form_terms_of_condition_checkbox_label_class).click()

    def sign_in(self, email, password):
        self.driver.find_element_by_id(self.account_button_id).click()
        self.logger.info(f'Passing email address: {email} to email input)')
        self.driver.find_element_by_name(self.login_form_email_input_name).send_keys(email)
        self.logger.info(f'Passing password: {password} to password input)')
        self.driver.find_element_by_name(self.login_form_password_input_name).send_keys(password)
        self.logger.info('Sending login form')
        self.driver.find_element_by_class_name(self.login_confirm_button_class).click()

    def go_to_account_page(self):
        time.sleep(2)
        self.driver.find_element_by_id(self.account_button_id).click()
        self.logger.info('Going to account settings page')
        self.driver.find_element_by_link_text(self.my_account_link_text).click()
        return self.driver.current_url













