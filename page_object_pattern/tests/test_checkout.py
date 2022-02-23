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
class TestCheckout:

    @allure.title('Test of using correct discount code during checkout')
    @allure.description('Sending correct discount code and checking message and summary correctness')
    def test_use_correct_discount_code(self, setup):
        self.driver.get('http://testshop.ovel.pl/m63-2')
        pdp = ProductDetailPage(self.driver)
        checkout = CheckoutPage(self.driver)
        code = 'sellingo'
        pdp.close_cookies_popup()
        pdp.add_to_basket()
        pdp.go_to_checkout_page()
        message = checkout.use_discount_code(code)
        summary = checkout.check_summary_correctness()
        assert message == 'Kod prawidłowy', "Nie wyświetlił się komunikat o poprawności kodu rabatowego"
        assert summary is True, "Cena produktu po rabacie nie zgadza się z wyświetlaną wartością rabatu"

    @allure.title('Test of using incorrect discount code during checkout')
    @allure.description('Sending incorrect discount code and checking error message')
    def test_use_incorrect_discount_code(self, setup):
        self.driver.get('http://testshop.ovel.pl/m63-2')
        pdp = ProductDetailPage(self.driver)
        checkout = CheckoutPage(self.driver)
        code = 'kodzik'
        pdp.close_cookies_popup()
        pdp.add_to_basket()
        pdp.go_to_checkout_page()
        message = checkout.use_discount_code(code)
        assert message == 'Kod nieprawidłowy', "Nie wyświetlił się komunikat o podaniu nieprawidłowego kodu rabatowego"

    @allure.title('Test of selecting parcel locker inside pop-up window')
    @allure.description('Sending parcel locker name, then selecting this locker and checking if address of locker which shows in checkout is correct')
    def test_select_inpost_point(self, setup):
        self.driver.get('http://testshop.ovel.pl/m63-2')
        pdp = ProductDetailPage(self.driver)
        checkout = CheckoutPage(self.driver)
        locker_name = 'WAW87N'
        delivery_method = 'Paczkomaty InPost'
        pdp.close_cookies_popup()
        pdp.add_to_basket()
        pdp.go_to_checkout_page()
        checkout.set_delivery_method(delivery_method)
        locker_address = checkout.set_parcel_locker(locker_name)
        #Adres w pop-upie ma inna kolejnosc niz ten pokazywany w koszyku - czekamy na poprawkie
        assert locker_address[0] in locker_address[1]







