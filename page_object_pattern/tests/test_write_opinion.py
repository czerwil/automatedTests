import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.product_card2 import ProductDetailPage



class TestWriteOpinion:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_write_opinion(self, setup):
        self.driver.get('http://prototype.devsel.pl/p/20/407/b2')
        pdp = ProductDetailPage(self.driver)
        pdp.close_cookies_popup()
        pdp.add_opinion('Konrad', 'Polecam', 4)
        pdp.send_opinion()

    def test_opinion_pagination(self, setup):
        self.driver.get('http://prototype.devsel.pl/p/20/446/apaszka-1')
        pdp = ProductDetailPage(self.driver)
        pdp.close_cookies_popup()
        pages = pdp.pagination_of_opinions()
        assert pages[0] == pages[1], "Błąd"




