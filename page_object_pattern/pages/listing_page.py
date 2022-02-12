import time
from re import match
import logging

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class ListingPage:

    def __init__(self, driver):
        self.driver = driver
        #self.logger =
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
        self.product_box_class = 'c-product-box--listing'
        self.search_query_title = 'c-section-header__title'
        self.sorting_container_class = 'js-select-field-action'
        self.min_price_input_class = 'js-price-filter-min-input'
        self.max_price_input_class = 'js-price-filter-max-input'
        self.price_filter_button_class = 'm-price-filter-1__button-wrapper'
        self.product_titles_class = 'at-product-box-title'
        self.product_primary_price_values_class = 'at-product-box-primary-price'
        self.pagination_module_class = 'm-pagination-1__page'
        self.pagination_next_page_class = 'm-pagination-1__nearby-page--next'
        self.pagination_last_page_class = 'm-pagination-1__page--last'
        self.pagination_active_page_class = "brakuje klasy"

    def accept_cookie_policy(self):
        self.driver.find_element_by_class_name(self.cookie_popup_accept_button_class).click()

    def get_results_titles(self, query):
        title_list = []
        try:
            pages_count = self.driver.find_elements_by_class_name(self.pagination_module_class)
            pages_count = int(pages_count[-1].text)
        except:
            for title in self.driver.find_elements_by_class_name(self.product_titles_class):
                title_list.append(title.text)
            return title_list
        for page in range(pages_count):
            for title in self.driver.find_elements_by_class_name(self.product_titles_class):
                title_list.append(title.text)
            if page + 1 == pages_count:
                return title_list
                break
            self.driver.find_element_by_class_name(self.pagination_next_page_class).click()

    def pagination(self):
        try:
            pages_count = self.driver.find_elements_by_class_name(self.pagination_module_class)
            pages_count = int(pages_count[-1].text)
        except:
            return 1
        for page in range(pages_count):
            if page + 1 == pages_count:
                break
            self.driver.find_element_by_class_name(self.pagination_next_page_class).click()
        last_page = self.driver.find_element_by_class_name(self.pagination_last_page_class).text
        return pages_count, last_page

    def products_sort(self, type):
        self.accept_cookie_policy()
        self.driver.find_element_by_class_name(self.sorting_container_class).click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,'c-select-field__list-holder')))
        self.driver.find_element_by_link_text(type).click()
        wait.until(expected_conditions.visibility_of_all_elements_located)
        if "Cena" in type:
            prices = self.driver.find_elements_by_class_name(self.product_primary_price_values_class)
            return prices
        if "Nazwa" in type:
            titles = self.driver.find_elements_by_class_name(self.product_titles_class)
            return titles

    def filter_by_price(self, price_min, price_max):
        self.accept_cookie_policy()
        self.driver.find_element_by_class_name(self.min_price_input_class).click()
        #self.driver.find_element_by_class_name(self.min_price_input_class).send_keys(Keys.BACK_SPACE*6)
        self.driver.find_element_by_class_name(self.min_price_input_class).clear()
        self.driver.find_element_by_class_name(self.min_price_input_class).send_keys(price_min)
        self.driver.find_element_by_class_name(self.max_price_input_class).click()
        #self.driver.find_element_by_class_name(self.max_price_input_class).send_keys(Keys.BACK_SPACE*6)
        self.driver.find_element_by_class_name(self.max_price_input_class).clear()
        self.driver.find_element_by_class_name(self.max_price_input_class).send_keys(price_max)
        self.driver.find_element_by_class_name(self.price_filter_button_class).click()
        prices = []
        try:
            pages_count = self.driver.find_elements_by_class_name(self.pagination_module_class)
            pages_count = int(pages_count[-1].text)
        except:
            prices = self.driver.find_elements_by_class_name(self.product_primary_price_values_class)
            return prices
        for page in range(pages_count):
            for price in self.driver.find_elements_by_class_name(self.product_primary_price_values_class):
                prices.append(price.text)
            if page + 1 == pages_count:
                return prices
                break
            self.driver.find_element_by_class_name(self.pagination_next_page_class).click()

        time.sleep(2)
















