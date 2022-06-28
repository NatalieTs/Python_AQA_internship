from test_selenium.site_methods import Site


class ContactPage(Site):
    @property
    def phone_element(self):
        return super().find_element('.contact-info__main-contacts .lohika-black-link')

    @property
    def mail_element(self):
        return super().find_element('.contact-info__main-contacts .lohika-link')

    def check_phone(self):
        self.phone_element.attribute_match('href', "tel:+16506366993")
        self.phone_element.text_match("+1 650 636 6993")
        return self

    def check_email(self):
        self.mail_element.attribute_match('href', "mailto:info@lohika.com")
        self.mail_element.text_match("info@lohika.com")
        return self

