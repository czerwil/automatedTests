import time

import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.homepage import Homepage


@pytest.mark.usefixtures('setup')
class TestHomePage:

    @allure.title('Test of newsletter subscription using correct e-mail address')
    @allure.description('Sending correct e-mail address and checking that pop-up comes up')
    def test_newsletter_subscribe_success(self, setup):
        self.driver.get('http://testshop.ovel.pl')
        homepage = Homepage(self.driver)
        homepage.close_cookies_popup()
        email_address = 'test@test.com'
        pop_up = homepage.subscribe_to_newsletter_success(email_address)
        assert pop_up!="", "Nie pojawił się pop-up potwierdzający zapisanie do newslettera"

    @allure.title('Test of newsletter subscription using incorrect e-mail address')
    @allure.description('Sending incorrect e-mail address and checking for an alert')
    def test_newsletter_subscribe_wrong_email(self, setup):
        self.driver.get('http://testshop.ovel.pl')
        homepage = Homepage(self.driver)
        homepage.close_cookies_popup()
        email_address = 'testtest.com'
        alert = homepage.subscribe_to_newsletter_fail(email_address)
        assert alert.text == 'Adres email jest nieprawidłowy.',"Komunikat jest niepoprawny"

    @allure.title('Test of going to specified category from header menu')
    @allure.description('Going to the category which matches passed link-text and checking that header and passed link-text matches')
    def test_menu_category_selection(self, setup):
        self.driver.get('http://testshop.ovel.pl')
        homepage = Homepage(self.driver)
        category = 'spodnie'
        is_correct = homepage.select_menu_category(category)
        assert is_correct is True, 'Nie udało się przejść do wybranej pozycji z menu'

    @allure.title('Test of products slider')
    @allure.description('Going to the category which matches passed link-text and checking that header and passed link-text matches')
    def test_products_slider(self, setup):
        self.driver.get('http://testshop.ovel.pl')
        homepage = Homepage(self.driver)
        homepage.close_cookies_popup()
        titles_before = homepage.get_products_titles_from_slider()
        homepage.slide_forward()
        titles_after = homepage.get_products_titles_from_slider()
        assert titles_before != titles_after, 'Nie działa slider, produkty się nie przesunęły'









