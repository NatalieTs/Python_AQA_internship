from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest
from test_selenium.main_page import MainPage


@pytest.fixture(scope='session')
def driver_setup():
    service = Service(executable_path=ChromeDriverManager().install())
    yield webdriver.Chrome(service=service)


@pytest.fixture(scope="function")
def main_page(driver_setup):
    site = MainPage(driver_setup)
    yield site
    site.close_site()

