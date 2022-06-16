import json
import os
import shutil

from contacts_manager.contact import Contact

from tabulate import tabulate
from contacts_manager.input_error import InputError


class ContactList:
    def __init__(self):
        self.list_contact = []


    def add_to_list(self, contact):
        self.list_contact.append(contact)
        self.contact_book()

    def contact_book(self):
        def to_dict(contact):
            return contact.__dict__
        contact_dict = map(to_dict, self.list_contact)
        with open("../../storage/contact_book.json", "w") as contact_book:
            json.dump(list(contact_dict), contact_book)
            for line in contact_dict:
                contact_book.write(line + '\n')
        contact_book.close()

    def from_dict(self):
        def to_contact(data):
            return Contact(**data)

        self.list_contact = []
        if os.path.exists("../../storage/contact_book.json"):
            with open("../../storage/contact_book.json", "r") as read_contact_book:
                contact_data = json.load(read_contact_book)
                self.list_contact = list(map(to_contact, contact_data))
            read_contact_book.close()

    def find(self, term):
        find_list = []
        for i in self.list_contact:
            if i.match(term):
                find_list.append(i)
        if len(find_list) == 0:
            print("You don't have this contact")
        else:
            table = []
            for c in find_list:
                table.append(c.fields())
            print(tabulate(table, headers=['Name', 'Phone', 'Email']))

    def print_all(self):
        table = []
        for i, c in enumerate(self.list_contact):
            table.append([i + 1] + c.fields())
        print(tabulate(table, headers=['Name', 'Phone', 'Email']))

    def delete_contact(self, delete):
        if delete not in range(1, len(self.list_contact) + 1):
            raise InputError('You dont have such contact!')
        self.list_contact.pop(delete - 1)
        print('The contact was removed')
