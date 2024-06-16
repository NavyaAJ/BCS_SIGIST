from selenium import webdriver
from selenium.webdriver.common.by import By

class NextHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, 'search-box-id')  # replace with actual ID

    def load(self):
        self.driver.get('https://www.next.co.uk/')  # replace with actual URL

    def search_product(self, product):
        self.driver.find_element(*self.search_box).send_keys(product)
        self.driver.find_element(*self.search_box).submit()