from phonenumbers import NumberParseException
from pyisemail import is_email
import phonenumbers

class Contact(object):
    def __init__(self, name, number, mail):
        self.name = name
        self.number = number
        self.mail = mail

    def match(self, term):
        return term in self.name or term in self.number

    def fields(self):
        return [self.name, self.number, self.mail]

    @staticmethod
    def check_email(contact_email):
        return is_email(contact_email)

    @staticmethod
    def check_phone(contact_phone):
        try:
            contact_number = phonenumbers.parse(contact_phone, None)
        except NumberParseException:
            return False
        return phonenumbers.is_valid_number(contact_number)

    @staticmethod
    def check_name(contact_name):
        return len(contact_name) >= 3
