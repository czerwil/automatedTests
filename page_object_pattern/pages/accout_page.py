import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver
        #self.logger =

