import pytest
import allure
from random import randrange
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.product_card2 import ProductDetailPage



class ProductDetailPage:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager(log_level=0).install())
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        yield
        self.driver.quit()

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
