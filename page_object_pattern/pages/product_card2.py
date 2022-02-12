import time

import logging
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



class ProductDetailPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.wishlist_button_id = 'header-wishlist'
        self.basket_button_id = 'header-cart'
        self.wishlist_count_class = 'js-display-wishlist-count'
        self.product_title_class = 'm-product-data-2__title'
        self.product_rating_class = 'm-product-data-2__rating'
        self.product_manufacturer_xpath = '/html/body/main/div[3]/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/span/a'
        self.product_catalog_number_class = 'js-product-catalog-number'
        self.product_prices_class = 'm-product-data-2__price-value'
        self.product_old_price_class = 'm-product-data-2__price--old'
        self.product_promotional_price_class = 'm-product-data-2__price--promotion'
        self.product_variants_scope_class = 'js-variants-scope'
        self.product_variant_color_class = 'js-product-color'
        self.product_variant_size_class = 'js-product-size'
        self.product_quantity_input_class = 'c-quantity-field__input'
        self.product_quantity_more_button_class = 'js-quantity-more'
        self.product_quantity_less_button_class = 'js-quantity-less'
        self.product_ask_about_product_class = 'm-product-data-2__ask'
        self.product_write_opinion_class = 'm-product-opinions-1__write-opinion'
        self.product_opinion_name = 'opinion_name'
        self.product_opinion_captcha = 'opinion_captcha'
        self.product_opinion_comment = 'opinion_comment'
        self.product_stars_class = 'js-select-rating'
        self.product_send_opinion_button_class = 'js-product-send-opinion'
        self.product_popup_message_class = 'l-popup__message'
        self.product_add_to_wishlist_button_class = 'js-product-card-wishlist-button'
        self.cookie_popup_accept_class = 'js-accept-cookie-alert-1'
        self.product_opinion_popup_close_class = 'l-popup__message-close'
        self.product_opinion_pagination_pages_class = 'm-pagination-1__page'
        self.product_opinion_next_page_button_class = 'm-pagination-1__nearby-page--next-opinions'
        self.product_opinion_last_page_button_class = 'm-pagination-1__page--last'
        self.product_add_to_basket_button_id = 'product-card-add-to-card'
        self.product_add_to_basket_button_error_class = 'js-add-product-to-card-error'
        self.product_add_to_basket_button_success_class = 'js-add-product-to-card-success'
        self.product_added_to_wishlist_tooltip_text_class = 'js-check-tooltip-text'
        self.product_add_to_basket_buttons_class = 'js-product-card-buttons'
        self.aside_redirect_to_basket_class = 'at-aside-cart-redirect'

    def set_variants(self):
        try:
            color = self.driver.find_element_by_class_name(self.product_variant_color_class).text
            self.logger.info('Setting color to {}'.format(color))
            self.driver.find_element_by_class_name(self.product_variant_color_class).click()
        except:
            pass
        try:
            size = self.driver.find_element_by_class_name(self.product_variant_size_class).text
            self.logger.info('Setting size to {}'.format(size))
            self.driver.find_element_by_class_name(self.product_variant_size_class).click()
        except:
            pass
        time.sleep(2)

    def add_to_wishlist(self):
        wait = WebDriverWait(self.driver, 5)
        product_name = self.driver.find_element_by_class_name(self.product_title_class).text
        self.driver.find_element_by_class_name(self.product_add_to_wishlist_button_class).click()
        time.sleep(1)
        #wait.until(expected_conditions.visibility_of((By.CLASS_NAME, self.product_added_to_wishlist_tooltip_text_class)))
        wishlist_count = self.driver.find_element_by_class_name(self.wishlist_count_class).text
        confirm_info = self.driver.find_element_by_class_name(self.product_added_to_wishlist_tooltip_text_class).text
        return confirm_info, wishlist_count, product_name

    def go_to_wishlist_page(self):
        self.driver.find_element_by_id(self.wishlist_button_id).click()
        self.driver.find_element_by_link_text('Ulubione').click()

    def add_to_basket(self):
        wait = WebDriverWait(self.driver, 5)
        try:
            product_name = self.driver.find_element_by_class_name(self.product_title_class).text
            product_price = self.driver.find_element_by_class_name(self.product_prices_class).text
            product_quantity = self.driver.find_element_by_class_name(self.product_quantity_input_class).get_attribute('value')
            wait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, self.product_add_to_basket_button_error_class)))
            self.driver.find_element_by_id(self.product_add_to_basket_button_id).click()
            time.sleep(1)
            self.logger.info('Added {} to basket successfully'.format(product_name))
            return product_name, product_price, product_quantity
        except:
            error_status = self.driver.find_element_by_class_name(self.product_add_to_basket_buttons_class).text
            self.logger.info(error_status)
            return error_status

    def add_opinion(self, name, opinion, stars):
        self.logger.info("Adding {stars} stars opinion with nickname {name}".format(stars=stars, name=name))
        self.driver.find_element_by_class_name(self.product_write_opinion_class).click()
        self.driver.find_element_by_name(self.product_opinion_name).send_keys(name)
        self.driver.find_element_by_name(self.product_opinion_captcha).send_keys('Warszawa')
        self.logger.info("Adding opinion text: {}".format(opinion))
        self.driver.find_element_by_name(self.product_opinion_comment).send_keys(opinion)
        rating = self.driver.find_elements_by_class_name(self.product_stars_class)
        rating[stars].click()

    def send_opinion(self):
        self.logger.info('Sending opinion')
        self.driver.find_element_by_class_name(self.product_send_opinion_button_class).click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, self.product_popup_message_class)))
        popup = self.driver.find_element_by_class_name(self.product_popup_message_class)
        return popup.is_displayed()


    def close_cookies_popup(self):
        self.driver.find_element_by_class_name(self.cookie_popup_accept_class).click()
        #self.driver.find_element_by_class_name(self.product_opinion_popup_close_class).click()

    def pagination_of_opinions(self):
        pages_count = self.driver.find_elements_by_class_name(self.product_opinion_pagination_pages_class)
        if len(pages_count)==0:
            self.logger.info("Pagination module not found")
            return 0
        pages_count = int(pages_count[-1].text)
        for page in range(pages_count):
            if page + 1 == pages_count:
                break
            time.sleep(0.4)
            try:
                self.logger.info(f"Going to page number {page+2}")
                self.driver.find_element_by_class_name(self.product_opinion_next_page_button_class).click()
            except:
                continue
        last_page = int(self.driver.find_element_by_class_name(self.product_opinion_last_page_button_class).text)
        self.logger.info(f"Last page number is {last_page}")
        return last_page, pages_count

    def go_to_checkout_page(self):
        self.driver.find_element_by_id(self.basket_button_id).click()
        self.driver.find_element_by_class_name(self.aside_redirect_to_basket_class).click()







