import time

import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.homepage import Homepage
from page_object_pattern.pages.accout_page import MyAccountPage


@pytest.mark.usefixtures('setup')
class TestLogIn:

    @allure.title('Test of logging in')
    @allure.description('Logging in to existing account and then going to the account page')
    def test_sign_in(self, setup):
        self.driver.get('http://tests-harmony.devsel.pl/')
        homepage = Homepage(self.driver)
        homepage.close_cookies_popup()
        homepage.sign_in('test@test.com', 'zaq12wsx')
        url = homepage.go_to_account_page()
        assert "/moje_konto" in url, "Niepoprawny adres strony - nie udało się przejść do strony Moje konto"

    @allure.title('Test of logging out')
    @allure.description('Logging in to existing account and then going to the account page and logging out, then checking that account page is not available')
    def test_sign_out(self,setup):
        self.driver.get('http://tests-harmony.devsel.pl/')
        homepage = Homepage(self.driver)
        account_page = MyAccountPage(self.driver)
        homepage.close_cookies_popup()
        homepage.sign_in('test@test.com', 'zaq12wsx')
        account_page_url = homepage.go_to_account_page()
        account_page.logout()
        self.driver.get('http://tests-harmony.devsel.pl/moje_konto')
        current_url = self.driver.current_url
        assert current_url != account_page_url, "Nie udało się wylogować - można przejść na stronę 'Moje konto'"


