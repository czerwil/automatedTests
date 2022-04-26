from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            capabilities = {
                "browserName": "chrome",
                "browserVersion": "99.0",
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": False
                }
            }
            options = webdriver.ChromeOptions()
            options.add_argument('start-maximized')
            driver = webdriver.Remote(
                command_executor="http://devsel.sellingo.pl:4444/wd/hub",
                desired_capabilities=capabilities,
                options=options)
            return driver
        elif browser == 'chrome_local':
            options = webdriver.ChromeOptions()
            options.add_argument('start-maximized')
            return webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        raise Exception("Provide valid driver name")

