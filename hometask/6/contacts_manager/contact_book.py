import json
import os
from contacts_manager.contact import *

PATH = os.path.join("..", "..", "storage", "contact_book.json")


def contact_book(list_contact):
    def to_dict(contact):
        return contact.__dict__

    contact_dict = map(to_dict, list_contact)
    with open(PATH, "w") as contact_book:
        json.dump(list(contact_dict), contact_book)
    contact_book.close()


def from_dict():
    def to_contact(data):
        return Contact(**data)

    list_contact = []
    if os.path.exists(PATH):
        with open(PATH, "r") as read_contact_book:
            contact_data = json.load(read_contact_book)
            list_contact = list(map(to_contact, contact_data))
        read_contact_book.close()
    return list_contact
