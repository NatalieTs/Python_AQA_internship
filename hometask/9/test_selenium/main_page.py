from test_selenium.site_methods import Site
from test_selenium.contact_us import ContactPage


class MainPage(Site):
    def open(self):
        super().open_site("https://www.lohika.com/")
        return self

    def go_to_contact_us_page(self):
        element = super().find_element("#menu-item-53 > a")
        element.click()
        return ContactPage(self.driver)
