import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.homepage import Homepage


@pytest.mark.usefixtures('setup')
class TestHomePage:

    def test_newsletter_subscribe_success(self, setup):
        self.driver.get('http://testshop.ovel.pl')
        homepage = Homepage(self.driver)
        homepage.close_cookies_popup()
        email_address = 'test@test.com'
        pop_up = homepage.subscribe_to_newsletter_success(email_address)
        assert pop_up!="", "Nie pojawił się pop-up potwierdzający zapisanie do newslettera"

    def test_newsletter_subscribe_wrong_email(self, setup):
        self.driver.get('http://testshop.ovel.pl')
        homepage = Homepage(self.driver)
        homepage.close_cookies_popup()
        email_address = 'testtest.com'
        alert = homepage.subscribe_to_newsletter_fail(email_address)
        assert alert.text == 'Adres email jest nieprawidłowy.',"Komunikat jest niepoprawny"

    def test_menu_category_selection(self, setup):
        self.driver.get('http://testshop.ovel.pl')
        homepage = Homepage(self.driver)
        category = 'spodnie'
        is_correct = homepage.select_menu_category(category)
        assert is_correct is True, 'Nie udało się przejść do wybranej pozycji z menu'






