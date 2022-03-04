import time

import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.homepage import Homepage
from page_object_pattern.pages.listing_page import ListingPage
from page_object_pattern.pages.product_card2 import ProductDetailPage
from page_object_pattern.pages.checkout import CheckoutPage


@pytest.mark.usefixtures('setup')
class TestPlaceOrder:

    @allure.title('Test of placing an order')
    @allure.description('Adding product to the basket and then going through the checkout and placing order')
    def test_place_order(self, setup):
        self.driver.get('http://testshop.ovel.pl/fanita')
        pdp = ProductDetailPage(self.driver)
        checkout = CheckoutPage(self.driver)
        pdp.close_cookies_popup()
        pdp.set_variants()
        is_product_available = pdp.add_to_basket()
        assert is_product_available != "Produkt niedostępny", "Produkt niedostępny"
        pdp.go_to_checkout_page()
        checkout.use_discount_code('SELLINGO')
        checkout.set_delivery_method('')
        checkout.set_payment_method('')
        value = checkout.check_summary_correctness()
        print(value)
        checkout.next_step()
        delivery_data = ['Jan', 'Kowalski', 'Szeroka', '14', '01-706', 'Warszawa', '500600900', 'k.czerwinski@netgraf.pl']
        checkout.complete_delivery_data(delivery_data)
        checkout.next_step()
        checkout.next_step()

    @allure.title('Test of placing an order')
    @allure.description('Adding product to the basket and then going through the checkout and placing order')
    def test_log_in_inside_checkout(self, setup):
        self.driver.get('http://testshop.ovel.pl/fanita')
        pdp = ProductDetailPage(self.driver)
        checkout = CheckoutPage(self.driver)
        pdp.close_cookies_popup()
        pdp.set_variants()
        is_product_available = pdp.add_to_basket()
        assert is_product_available != "Produkt niedostępny", "Wybrany wariant produktu jest niedostępny"
        pdp.go_to_checkout_page()
        products_data = checkout.get_product_data()
        checkout.next_step()
        checkout.login_inside_checkout(['test@test.com','zaq12wsx'])
        time.sleep(5)
        products_data_after_login = checkout.get_product_data()
        assert products_data == products_data_after_login, 'Po zalogowaniu się w koszyku zniknęły wcześniej dodane produkty'
        checkout.remove_product_from_the_cart()






#def test_summary_correctness(self, setup):




