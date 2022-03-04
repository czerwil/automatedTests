import time

import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.homepage import Homepage
from page_object_pattern.pages.listing_page import ListingPage
from page_object_pattern.pages.product_card2 import ProductDetailPage
from page_object_pattern.pages.checkout import CheckoutPage
from page_object_pattern.pages.wishlist import WishlistPage


@pytest.mark.usefixtures('setup')
class TestWishlist:

    @allure.title('Test of adding product from pdp to the wishlist')
    @allure.description('Adding product to wishlist from the product detail page')
    def test_add_product_to_wishlist(self, setup):
        self.driver.get('http://testshop.ovel.pl/sabi')
        pdp = ProductDetailPage(self.driver)
        wishlist = WishlistPage(self.driver)
        pdp.close_cookies_popup()
        pdp.set_variants()
        info = pdp.add_to_wishlist()
        pdp.go_to_wishlist_page()
        assert info[0] == 'Dodano do ulubionych', "Powiadomienie o dodaniu produktu do ulubionych sie nie wyświetliło"
        assert info[1] == '1', 'Nie wyświetlił się licznik produktów przy ikonce ulubione'
        product_title = wishlist.get_product_title()
        assert info[2] == product_title, "Tytuł produktu z wishlisty nie jest taki sam jak tytul na karcie produktu"

    @allure.title('Test of adding product from wishlist to the basket')
    @allure.description('Adding product to wishlist and then going to the wishlist page and adding product from there to the basket')
    def test_add_product_do_card_from_wishlist(self, setup):
        self.driver.get('http://testshop.ovel.pl/sabi')
        pdp = ProductDetailPage(self.driver)
        wishlist = WishlistPage(self.driver)
        pdp.close_cookies_popup()
        pdp.set_variants()
        info = pdp.add_to_wishlist()
        pdp.go_to_wishlist_page()
        cart_info = wishlist.add_all_products_to_basket()
        assert cart_info[0] == info[1], "Niepoprawna ilość produktów w koszyku"
        assert cart_info[1] == info[2], "Niepoprawny produkt został dodany do koszyka"

        



