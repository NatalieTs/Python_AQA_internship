import json

from contacts_manager.contact import Contact
from contacts_manager.contactlist import ContactList
from contacts_manager.input_error import InputError
import atexit

class Dispatcher:
    def __init__(self):
        self.cl = ContactList()
        self.cl.from_dict()
        atexit.register(self.cl.contact_book)

        self.intro()


    def get_valid_name(self):
        contact_name = input('Enter the name ')
        while not Contact.check_name(contact_name):
            print('Your name is less than 3 letters')
            contact_name = input('Enter the name of a contact ')
        return contact_name

    def get_valid_number(self):
        contact_number = input('Enter the number of a contact ')
        while not Contact.check_phone(contact_number):
            print('Your phone number is invalid')
            contact_number = input('Enter the number of a contact ')
        return contact_number

    def get_valid_email(self):
        contact_email = input('Enter e-mail address of a contact ')
        while not Contact.check_email(contact_email):
            print('Your email is invalid')
            contact_email = input('Enter e-mail address of a contact ')
        return contact_email

    def check_input(self, choice):
        if int(choice) not in range(1, 6):
            raise InputError('Enter the correct number')


    def intro(self):
        print("That is your Contact Book. You have next options:\n 1 - add contact\n 2 - find contact\n 3 - receive the whole list of contacts\n 4 - exit the Contact Book\n 5 - remove the contact\n")
        while True:
            try:
                user_choice = input('Make your choice ')
                self.check_input(user_choice)
                if user_choice == '1':
                    contact_name = self.get_valid_name()
                    contact_number = self.get_valid_number()
                    contact_email = self.get_valid_email()

                    new_contact = Contact(contact_name, contact_number, contact_email)
                    self.cl.add_to_list(new_contact)
                    print('New contact has been added')
                elif user_choice == '2':
                    term = input('please, type your term ')
                    self.cl.find(term)
                elif user_choice == '3':
                    self.cl.print_all()
                elif user_choice == '4':
                    print('Bye')
                    break
                elif user_choice == '5':
                    remove = int(input('Enter the index of a contact to delete '))
                    self.cl.delete_contact(remove)
            except InputError as error:
                print(error.value)
            except ValueError:
                print('Enter the correct number')
