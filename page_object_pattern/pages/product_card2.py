import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class ProductDetailPage:

    def __init__(self, driver):
        self.driver = driver
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
        self.product_quantity_input_class = 'js-product-quantity'
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

    def set_variants(self):
        self.driver.find_element_by_class_name(self.product_variant_color_class).click()
        self.driver.find_element_by_class_name(self.product_variant_size_class).click()
        time.sleep(2)

    def add_to_wishlist(self):
        self.driver.find_element_by_class_name(self.product_add_to_wishlist_button_class).click()
        product_name = self.driver.find_element_by_class_name(self.product_title_class).text
        return product_name

    def add_to_basket(self):
        wait = WebDriverWait(self.driver, 3)
        try:
            product_name = self.driver.find_element_by_class_name(self.product_title_class).text
            wait.until(expected_conditions.element_to_be_clickable((By.ID, self.product_add_to_basket_button_id)))
            self.driver.find_element_by_id(self.product_add_to_basket_button_id).click()
            time.sleep(1)
            self.driver.find_element_by_class_name(self.product_add_to_basket_button_success_class).click()
            return product_name
        except:
            error_status = self.driver.find_element_by_class_name(self.product_add_to_basket_button_error_class).text
            return error_status


    def add_opinion(self, name, opinion, stars):
        self.driver.find_element_by_class_name(self.product_write_opinion_class).click()
        self.driver.find_element_by_name(self.product_opinion_name).send_keys(name)
        self.driver.find_element_by_name(self.product_opinion_captcha).send_keys('Warszawa')
        self.driver.find_element_by_name(self.product_opinion_comment).send_keys(opinion)
        rating = self.driver.find_elements_by_class_name(self.product_stars_class)
        rating[stars].click()

    def send_opinion(self):
        self.driver.find_element_by_class_name(self.product_send_opinion_button_class).click()

    def close_cookies_popup(self):
        self.driver.find_element_by_class_name(self.cookie_popup_accept_class).click()
        #self.driver.find_element_by_class_name(self.product_opinion_popup_close_class).click()

    def pagination_of_opinions(self):
        pages_count = self.driver.find_elements_by_class_name(self.product_opinion_pagination_pages_class)
        pages_count = int(pages_count[-1].text)
        for page in range(pages_count):
            if page + 1 == pages_count:
                break
            time.sleep(0.4)
            try:
                self.driver.find_element_by_class_name(self.product_opinion_next_page_button_class).click()
            except:
                continue
        last_page = int(self.driver.find_element_by_class_name(self.product_opinion_last_page_button_class).text)
        return last_page, pages_count







