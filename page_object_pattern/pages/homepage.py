import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

class Homepage:

    def __init__(self, driver):
        self.driver = driver
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

    def perform_search(self,query):
        self.driver.find_element_by_id(self.search_query_id).click()
        self.driver.find_element_by_id(self.search_query_id).send_keys(query + Keys.ENTER)

    def accept_cookie_policy(self):
        self.driver.find_element_by_class_name(self.cookie_popup_accept_button_class).click()

    def subscribe_to_newsletter(self, email):
        self.driver.find_element_by_class_name(self.newsletter_email_input_class).send_keys(email)
        self.driver.find_element_by_class_name(self.newsletter_submit_button_class).click()
        alert = self.driver.find_element_by_xpath(self.newsletter_alert_span_xpath)
        time.sleep(1)
        return alert







