import time
import logging

import allure
from allure_commons.types import AttachmentType
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
        self.menu_items_class = 'js-menu-1-item'
        self.listing_header_class = 'at-listing-header'
        self.slider_next_button_class = 'js-products-slider-1-next'
        self.slider_previous_button_class = 'js-products-slider-1-prev'
        self.homepage_product_title_class = 'at-product-box-title'
        self.homepage_banner_swiper_pagination_bullet_class = 'swiper-pagination-bullet'
        self.homepage_banner_swiper_pagination_bullet_active_class = 'swiper-pagination-bullet-active'
        self.homepage_banner_image_class = 'c-banner-element__image'


    @allure.step('Performing search')
    def perform_search(self,query):
        self.logger.info('Performing search of: {}'.format(query))
        self.driver.find_element_by_id(self.search_query_id).click()
        self.driver.find_element_by_id(self.search_query_id).send_keys(query + Keys.ENTER)
        allure.attach(self.driver.get_screenshot_as_png(), name='performing search',
                      attachment_type=AttachmentType.PNG)

    @allure.step('Closing the cookies popup')
    def close_cookies_popup(self):
        self.driver.find_element_by_class_name(self.cookie_popup_accept_button_class).click()

    @allure.step('Trying to subscribe to newsletter with incorrect e-mail address')
    def subscribe_to_newsletter_fail(self, email):
        self.logger.info("Subscribing for newsletter:")
        self.logger.info("Sending email address{}".format(email))
        self.driver.find_element_by_class_name(self.newsletter_email_input_class).send_keys(email)
        self.logger.info("Clicking subscribe button")
        self.driver.find_element_by_class_name(self.newsletter_submit_button_class).click()
        time.sleep(1)
        alert = self.driver.find_element_by_xpath(self.newsletter_alert_span_xpath)
        self.logger.info("Got alert message: {}".format(alert.text))
        allure.attach(self.driver.get_screenshot_as_png(), name='incorrect email address',
                      attachment_type=AttachmentType.PNG)
        return alert

    @allure.step('Trying to subscribe to newsletter with correct e-mail address')
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
        allure.attach(self.driver.get_screenshot_as_png(), name='subscribed to newsletter',
                      attachment_type=AttachmentType.PNG)
        return pop_up_text

    @allure.step('Registering a new account')
    def register_account(self, email, password):
        self.driver.find_element_by_id(self.account_button_id).click()
        self.driver.find_element_by_class_name(self.switch_to_register_form_class).click()
        self.driver.find_element_by_name(self.login_form_email_input_name).send_keys(email)
        self.driver.find_element_by_name(self.login_form_password_input_name).send_keys(password)
        self.driver.find_element_by_name(self.login_form_confirm_password_input_name).send_keys(password)
        self.driver.find_element_by_class_name(self.register_form_terms_of_condition_checkbox_label_class).click()

    @allure.step('Logging in to an existing account')
    def sign_in(self, email, password):
        self.driver.find_element_by_id(self.account_button_id).click()
        self.logger.info(f'Passing email address: {email} to email input)')
        self.driver.find_element_by_name(self.login_form_email_input_name).send_keys(email)
        self.logger.info(f'Passing password: {password} to password input)')
        self.driver.find_element_by_name(self.login_form_password_input_name).send_keys(password)
        self.logger.info('Sending login form')
        self.driver.find_element_by_class_name(self.login_confirm_button_class).click()
        allure.attach(self.driver.get_screenshot_as_png(), name='logging in',
                      attachment_type=AttachmentType.PNG)

    @allure.step('Redirecting to the account page')
    def go_to_account_page(self):
        time.sleep(2)
        self.driver.find_element_by_id(self.account_button_id).click()
        self.logger.info('Going to account settings page')
        self.driver.find_element_by_link_text(self.my_account_link_text).click()
        allure.attach(self.driver.get_screenshot_as_png(), name='redirecting to the account page',
                      attachment_type=AttachmentType.PNG)
        return self.driver.current_url

    @allure.step('Selecting passed category on header menu')
    def select_menu_category(self, category):
        wait = WebDriverWait(self.driver,3)
        menu_items = self.driver.find_elements_by_class_name(self.menu_items_class)
        menu_items_names = []
        for item in menu_items:
            menu_items_names.append(item.text)
        self.logger.info('There are {} menu items: {}'.format(len(menu_items),menu_items_names))
        for item in menu_items:
            if item.text == category:
                self.logger.info('Clicking on {}'.format(item.text))
                selected_item = item.text
                item.click()
                break
        wait.until(expected_conditions.url_changes)
        listing_header = self.driver.find_element_by_class_name(self.listing_header_class).text
        self.logger.info('Successful redirect to the {}'.format(listing_header))
        allure.attach(self.driver.get_screenshot_as_png(), name='redirected to the selected menu category',
                      attachment_type=AttachmentType.PNG)
        return selected_item == listing_header

    @allure.step('Clicking slider next button')
    def slide_forward(self):
        self.driver.find_element_by_class_name(self.slider_next_button).click()
        allure.attach(self.driver.get_screenshot_as_png(), name='sliding through product slider',
                      attachment_type=AttachmentType.PNG)
        time.sleep(1)

    @allure.step('Clicking slider previous button')
    def slide_back(self):
        self.driver.find_element_by_class_name(self.slider_previous_button).click()
        allure.attach(self.driver.get_screenshot_as_png(), name='sliding through product slider',
                      attachment_type=AttachmentType.PNG)
        time.sleep(1)

    @allure.step('Getting actually visible titles of products from slider')
    def get_products_titles_from_slider(self):
        titles = self.driver.find_elements_by_class_name(self.homepage_product_title)
        visible_titles = []
        for title in titles:
            if len(title.text) > 0:
                visible_titles.append(title.text)
        return visible_titles

    @allure.step('Swiping through banner images')
    def use_banner_swiper(self):
        swiper_bullets = self.driver.find_elements_by_class_name(self.homepage_banner_swiper_pagination_bullet_class)
        for bullet in swiper_bullets:
            self.logger.info('Swiping to the next banner')
            bullet.click()
            time.sleep(0.5)
            allure.attach(self.driver.get_screenshot_as_png(), name='sliding through banner slider',
                          attachment_type=AttachmentType.PNG)

    @allure.step('Clicking on currently visible banner')
    def click_on_visible_banner(self):
        banner_images = self.driver.find_elements_by_class_name(self.homepage_banner_image_class)
        for image in banner_images:
            if image.is_displayed():
                try:
                    image.click()
                except:
                    self.logger.info("Tried to click on not visible banner")
        allure.attach(self.driver.get_screenshot_as_png(), name='clicked on banner and redirected',
                      attachment_type=AttachmentType.PNG)































