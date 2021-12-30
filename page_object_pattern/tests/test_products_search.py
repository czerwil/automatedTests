import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.homepage import Homepage
from page_object_pattern.pages.listing_page import ListingPage


class TestProductsSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_search_product(self, setup):
        self.driver.get('http://prototype1.devsel.pl')
        query = 'MOE'
        homepage = Homepage(self.driver)
        homepage.perform_search(query)
        listing = ListingPage(self.driver)
        titles = listing.get_results_titles(query)
        #Sprawdzenie czy wyszukana fraza zawiera się w wyszukanych nazwach produktów
        for title in titles:
            assert query in title, "Szukana fraza '" + query + "' nie znajduje sie w wyniku wyszukiwania " + title

    def test_listing_pagination(self, setup):
        self.driver.get('http://prototype1.devsel.pl')
        homepage = Homepage(self.driver)
        listing = ListingPage(self.driver)
        homepage.perform_search('Czarny')
        pages = listing.pagination()
        # Sprawdzenie, czy udało się przejść do ostatniej strony paginacji na listingu
        assert pages[0] == int(pages[1]), "Stron powinno być " + str(pages[0]) + ", a ostatnia strona ma numer " + pages[1]

    def test_sort_by_price_asc(self, setup):
        self.driver.get('http://prototype1.devsel.pl/produkty/nowosci')
        listing = ListingPage(self.driver)
        prices = listing.products_sort('Cena rosnąco')
        cheaper = float(prices[0].text.replace(",", "."))
        for price in prices:
            price_value = float(price.text.replace(',', '.'))
            assert cheaper <= price_value, "Blad w sortowaniu po cenie"
            cheaper = price_value

    def test_sort_by_price_desc(self, setup):
        self.driver.get('http://prototype1.devsel.pl/produkty/nowosci')
        listing = ListingPage(self.driver)
        prices = listing.products_sort('Cena malejąco')
        more_expensive = float(prices[0].text.replace(",", "."))
        for price in prices:
            price_value = float(price.text.replace(',', '.'))
            assert more_expensive >= price_value, "Blad w sortowaniu po cenie"
            more_expensive = price_value

    def test_sort_by_name_asc(self, setup):
        self.driver.get('http://prototype1.devsel.pl/produkty/nowosci')
        listing = ListingPage(self.driver)
        titles = listing.products_sort('Nazwa rosnąco')
        first_title = titles[0].text
        for title in titles:
            assert first_title <= title.text, "Blad w sortowaniu po nazwie"
            first_title = title.text

    def test_sort_by_name_desc(self, setup):
        self.driver.get('http://prototype1.devsel.pl/produkty/nowosci')
        listing = ListingPage(self.driver)
        titles = listing.products_sort('Nazwa malejąco')
        first_title = titles[0].text.lower()
        for title in titles:
            next_title = title.text.lower()
            assert first_title >= next_title, "Blad w sortowaniu po nazwie"
            first_title = next_title

    def test_filtering_products(self, setup):
        self.driver.get('http://prototype1.devsel.pl/produkty/nowosci')
        min = 50
        max = 80
        listing = ListingPage(self.driver)
        prices = listing.filter_by_price(min, max)
        #pobierają się dwie ceny z produktu regularna i promocyjna - need fix
        for price in prices:
            price_value = float(price.replace(',', '.'))
            assert price_value >= min and price_value <= max, "Błąd w filtrowaniu po cenie"





