import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.homepage import Homepage
from page_object_pattern.pages.listing_page import ListingPage
from page_object_pattern.pages.product_card2 import ProductDetailPage
from page_object_pattern.pages.checkout import CheckoutPage
from page_object_pattern.pages.wishlist import WishlistPage


class TestAddToWishlist:

    @pytest.fixture()
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")
        #options.add_argument("--headless")
        options.add_argument('window-size=1920x1080');
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_add_product_to_wishlist(self, setup):
        self.driver.get('http://prototype.devsel.pl/p/13/182/m080-1')
        pdp = ProductDetailPage(self.driver)
        wishlist = WishlistPage(self.driver)
        pdp.set_variants()
        info = pdp.add_to_wishlist()
        assert info[0] == 'Dodano do ulubionych', "Powiadomienie o dodaniu produktu do ulubionych sie nie wyświetliło"
        product_title = wishlist.get_product_title()
        assert info[1] == product_title, "Tytuł produktu z wishlisty nie jest taki sam jak tytul na karcie produktu"

    #def test_add_product_do_card_from_wishlist(self, setup):
        



