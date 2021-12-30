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
        self.driver.get('http://prototype1.devsel.pl/p/20/343/moe069-2')
        pdp = ProductDetailPage(self.driver)
        checkout = CheckoutPage(self.driver)
        pdp.close_cookies_popup()
        pdp.set_variants()
        pdp.add_to_basket()
        checkout.set_delivery_method()
        checkout.set_payment_method()
        checkout.use_discount_code('test10')

