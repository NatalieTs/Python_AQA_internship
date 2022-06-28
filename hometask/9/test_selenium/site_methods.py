from test_selenium.item import Item
from selenium.webdriver.common.by import By


class Site(object):
    def __init__(self, driver):
        self.driver = driver

    def open_site(self, site_url):
        self.driver.get(site_url)

    def find_element(self, matcher, by=By.CSS_SELECTOR):
        return Item(self.driver.find_element(value=matcher, by=by))

    def close_site(self):
        self.driver.quit()

