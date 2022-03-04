import allure
import pytest
from page_object_pattern.pages.homepage import Homepage
from page_object_pattern.pages.listing_page import ListingPage


@pytest.mark.usefixtures('setup')
class TestListing:

    @allure.title('Test of search form')
    @allure.description('Typing query in search form and then performing search and checking that results are matching the search query')
    def test_search_product(self, setup):
        self.driver.get('http://testshop.ovel.pl')
        query = 'MOE'
        homepage = Homepage(self.driver)
        homepage.perform_search(query)
        listing = ListingPage(self.driver)
        titles = listing.get_results_titles(query)
        for title in titles:
            assert query in title, "Szukana fraza '" + query + "' nie znajduje sie w wyniku wyszukiwania " + title

    @allure.title('Test of listing pagination')
    @allure.description('Searching for products and then paginating through all listing pages')
    def test_listing_pagination(self, setup):
        self.driver.get('http://testshop.ovel.pl')
        homepage = Homepage(self.driver)
        listing = ListingPage(self.driver)
        homepage.perform_search('MOE')
        pages = listing.pagination()
        assert pages[0] == int(pages[1]), "Stron powinno być " + str(pages[0]) + ", a ostatnia strona ma numer " + pages[1]

    @allure.title('Test of sorting products by price ascending')
    @allure.description('Searching for products and then sorting them by price ascending')
    def test_sort_by_price_asc(self, setup):
        self.driver.get('http://testshop.ovel.pl/bluzki')
        listing = ListingPage(self.driver)
        prices = listing.products_sort('Cena rosnąco')
        cheaper = float(prices[0].text.replace(",", "."))
        for price in prices:
            price_value = float(price.text.replace(',', '.'))
            assert cheaper <= price_value, "Blad w sortowaniu po cenie"
            cheaper = price_value

    @allure.title('Test of sorting products by price descending')
    @allure.description('Searching for products and then sorting them by price descending')
    def test_sort_by_price_desc(self, setup):
        self.driver.get('http://testshop.ovel.pl/bluzki')
        listing = ListingPage(self.driver)
        prices = listing.products_sort('Cena malejąco')
        more_expensive = float(prices[0].text.replace(",", "."))
        for price in prices:
            price_value = float(price.text.replace(',', '.'))
            assert more_expensive >= price_value, "Blad w sortowaniu po cenie"
            more_expensive = price_value

    @allure.title('Test of sorting products by name ascending')
    @allure.description('Searching for products and then sorting them by name ascending')
    def test_sort_by_name_asc(self, setup):
        self.driver.get('http://testshop.ovel.pl/bluzki')
        listing = ListingPage(self.driver)
        titles = listing.products_sort('Nazwa rosnąco')
        first_title = titles[0].text
        for title in titles:
            assert first_title <= title.text, "Blad w sortowaniu po nazwie"
            first_title = title.text

    @allure.title('Test of sorting products by name descending')
    @allure.description('Searching for products and then sorting them by name descending')
    def test_sort_by_name_desc(self, setup):
        self.driver.get('http://testshop.ovel.pl/bluzki')
        listing = ListingPage(self.driver)
        titles = listing.products_sort('Nazwa malejąco')
        first_title = titles[0].text.lower()
        for title in titles:
            next_title = title.text.lower()
            assert first_title >= next_title, "Blad w sortowaniu po nazwie"
            first_title = next_title

    @allure.title('Test of filtering products by price')
    @allure.description('Filtering products by price and then checking that prices of products are in selected range')
    def test_filtering_products(self, setup):
        self.driver.get('http://testshop.ovel.pl/bluzki')
        min = 50
        max = 80
        listing = ListingPage(self.driver)
        prices = listing.filter_by_price(min, max)
        for price in prices:
            price_value = float(price.replace(',', '.'))
            assert price_value >= min and price_value <= max, "Błąd w filtrowaniu po cenie"

#Inputy w filtrach po wyczyszczeniu i zgubieniu focusa automatycznie się uzupełniają przez co nie mogę wprowadzić wartości




