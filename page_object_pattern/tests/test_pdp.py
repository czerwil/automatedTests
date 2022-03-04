from random import randrange
import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.homepage import Homepage
from page_object_pattern.pages.listing_page import ListingPage
from page_object_pattern.pages.product_card2 import ProductDetailPage
from page_object_pattern.pages.checkout import CheckoutPage


@pytest.mark.usefixtures('setup')
class TestProductDetailPage:

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

    @allure.title('Test of adding new opinion')
    @allure.description('Writing and sending opinion of product')
    def test_write_opinion(self, setup):
        self.driver.get('http://testshop.ovel.pl/sabi')
        pdp = ProductDetailPage(self.driver)
        pdp.close_cookies_popup()
        pdp.add_opinion('Konrad', 'Polecam', randrange(1, 5))
        is_popup_displayed = pdp.send_opinion()
        assert is_popup_displayed is True, "Nie wyświetlił się pop-up potwierdzający dodanie opinii produktu"

    @allure.title('Test of opinion paginations')
    @allure.description('Paginating through all opinions pages')
    def test_opinion_pagination(self, setup):
        self.driver.get('http://testshop.ovel.pl/sabi')
        pdp = ProductDetailPage(self.driver)
        pdp.close_cookies_popup()
        pages = pdp.pagination_of_opinions()
        assert pages[0] == pages[1], "Błąd - nie można przejść do wszystkich stron paginacji opinii"

    @allure.title('Test of setting option')
    @allure.description('Selecting image option of the product')
    def test_select_option(self, setup):
        self.driver.get('http://testshop.ovel.pl/k089-1')
        pdp = ProductDetailPage(self.driver)
        pdp.close_cookies_popup()
        options = pdp.set_option()
        assert options[0] == options[1], "Nazwa wybranej opcji nie wyświetla się"






