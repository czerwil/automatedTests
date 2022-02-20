import random
import allure
import pytest
from page_object_pattern.pages.homepage import Homepage


@pytest.mark.usefixtures('setup')
class TestAddProductsToBasket:

    @allure.title('Test of registration new account')
    @allure.description('')
    def test_search_product(self, setup):
        self.driver.get('http://testshop.ovel.pl')
        email = 'test@test.com'
        password = 'zaq12wsx'
        homepage = Homepage(self.driver)
        homepage.register_account(email, password)


