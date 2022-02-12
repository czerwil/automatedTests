import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.homepage import Homepage
from page_object_pattern.pages.accout_page import MyAccountPage


class TestRegisterAccount:

    @pytest.fixture()
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")
        #options.add_argument("--headless")
        options.add_argument('window-size=1920x1080');
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.implicitly_wait(8)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_sign_in(self, setup):
        self.driver.get('http://testshop.ovel.pl')
        homepage = Homepage(self.driver)
        homepage.accept_cookie_policy()
        homepage.sign_in('test@test.com', 'zaq12wsx')
        url = homepage.go_to_account_page()
        assert url == 'http://testshop.ovel.pl/moje_konto', "Niepoprawny adres strony - nie udało się przejść do strony Moje konto"

    def test_sign_out(self,setup):
        self.driver.get('http://testshop.ovel.pl')
        homepage = Homepage(self.driver)
        account_page = MyAccountPage(self.driver)
        homepage.accept_cookie_policy()
        homepage.sign_in('test@test.com', 'zaq12wsx')
        account_page_url = homepage.go_to_account_page()
        account_page.logout()
        self.driver.get('http://testshop.ovel.pl/moje_konto')
        current_url = self.driver.current_url
        assert current_url != account_page_url, "Nie udało się wylogować - można przejść na stronę 'Moje konto'"


