import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.homepage import Homepage
from page_object_pattern.pages.listing_page import ListingPage
from page_object_pattern.pages.product_card2 import ProductDetailPage
from page_object_pattern.pages.checkout import CheckoutPage

class TestPlaceOrder:

    @pytest.fixture()
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")
        #options.add_argument("--headless")
        options.add_argument('window-size=1920x1080');
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        yield
        self.driver.quit()
    
    def test_place_order(self, setup):
        self.driver.get('http://testshop.ovel.pl/fanita')
        pdp = ProductDetailPage(self.driver)
        checkout = CheckoutPage(self.driver)
        pdp.close_cookies_popup()
        pdp.set_variants()
        is_product_available = pdp.add_to_basket()
        assert is_product_available != "Produkt niedostępny", "Produkt niedostępny"
        checkout.use_discount_code('SELLINGO')
        checkout.set_delivery_method()
        checkout.set_payment_method()
        value = checkout.check_summary_correctness()
        print(value)
        checkout.next_step()
        delivery_data = ['Jan', 'Kowalski', 'Szeroka', '14', '01-706', 'Warszawa', '500600900', 'k.czerwinski@netgraf.pl']
        checkout.complete_delivery_data(delivery_data)
        checkout.next_step()

        checkout.next_step()

    #def log_in_inside_checkout(self, setup):

    #def test_summary_correctness(self, setup):




