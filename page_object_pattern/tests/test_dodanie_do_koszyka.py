import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.homepage import Homepage
from page_object_pattern.pages.listing_page import ListingPage
from page_object_pattern.pages.product_card2 import ProductDetailPage

class TestAddProductsToBasket:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_add_single_product_to_basket(self, setup):
        self.driver.get('http://prototype.devsel.pl/p/20/407/b2')
        pdp = ProductDetailPage(self.driver)
        pdp.set_variants()
        added_product_name = pdp.add_to_basket()
        print(added_product_name)


