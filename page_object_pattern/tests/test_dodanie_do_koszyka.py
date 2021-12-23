import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.homepage import Homepage
from page_object_pattern.pages.listing_page import ListingPage
from page_object_pattern.pages.product_card2 import ProductDetailPage
from page_object_pattern.pages.checkout import CheckoutPage

class TestAddProductsToBasket:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_add_single_product_to_basket(self, setup):
        self.driver.get('http://prototype.devsel.pl/p/20/343/moe069-2')
        pdp = ProductDetailPage(self.driver)
        basket = CheckoutPage(self.driver)
        pdp.close_cookies_popup()
        pdp.set_variants()
        pdp_data = pdp.add_to_basket()
        basket_data = basket.get_product_data()
        assert pdp_data == basket_data, "Nazwa produktu w koszyku jest nieprawidłowa"



