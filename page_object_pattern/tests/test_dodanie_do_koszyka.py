import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.homepage import Homepage
from page_object_pattern.pages.listing_page import ListingPage
from page_object_pattern.pages.product_card2 import ProductDetailPage
from page_object_pattern.pages.checkout import CheckoutPage


@pytest.mark.usefixtures('setup')
class TestAddProductsToBasket:

    @allure.title('Test of adding single product to the basket')
    @allure.description("Adding single product from product detail page to the basket")
    def test_add_single_product_to_basket(self, setup):
        self.driver.get('http://testshop.ovel.pl/sabi')
        pdp = ProductDetailPage(self.driver)
        basket = CheckoutPage(self.driver)
        pdp.close_cookies_popup()
        pdp.set_variants()
        pdp_data = pdp.add_to_basket()
        pdp.go_to_checkout_page()
        basket_data = basket.get_product_data()
        assert pdp_data == basket_data, "Nazwa produktu w koszyku jest nieprawidłowa"

#zeby porownac warianty trzeba wyodrebnic w koszyku wartosc wariantu od jego nazwy


