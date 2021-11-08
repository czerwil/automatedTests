import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.homepage import Homepage

class TestNewsletterSubscription:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_subscribe_success(self, setup):
        self.driver.get('http://prototype.devsel.pl')
        homepage = Homepage(self.driver)
        homepage.accept_cookie_policy()
        email_address = 'test@test.com'
        homepage.subscribe_to_newsletter(email_address)

    def test_subscribe_wrong_email(self, setup):
        self.driver.get('http://prototype.devsel.pl')
        homepage = Homepage(self.driver)
        homepage.accept_cookie_policy()
        email_address = 'testtest.com'
        alert = homepage.subscribe_to_newsletter(email_address)
        assert alert.text == 'Adres email jest nieprawidłowy.',"Komunikat jest niepoprawny"


