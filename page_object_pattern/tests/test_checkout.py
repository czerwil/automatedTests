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

    @allure.title('Test of removing product from the basket')
    @allure.description('Adding single product to the basket and then removing it and checking if it is not present')
    def test_remove_product_from_basket(self, setup):
        self.driver.get('http://testshop.ovel.pl/m63-2')
        pdp = ProductDetailPage(self.driver)
        checkout = CheckoutPage(self.driver)
        pdp.close_cookies_popup()
        pdp.add_to_basket()
        pdp.go_to_checkout_page()
        before = checkout.get_product_data()
        checkout.remove_product_from_the_cart()
        assert checkout.check_that_basket_is_empty() == True, "Koszyk nie został opróżniony"

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
        time.sleep(1)

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









