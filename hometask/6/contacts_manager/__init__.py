from contacts_manager.contact import Contact
from contacts_manager.contactlist import ContactList

class Dispatcher:
    def __init__(self):
        self.cl = ContactList()
        self.intro()

    def intro(self):
        print("That is your Contact Book. You have next options:\n 1 - add contact\n 2 - find contact\n 3 - receive the whole list of contacts\n 4 - exit the Contact Book\n 5 - remove the contact\n")
        while True:
            user_choice = input('Make your choice ')
            if user_choice == '1':
                contact_name = input('Enter the name ')
                while not Contact.check_name(contact_name):
                    print('Your name is less than 3 letters')
                    contact_name = input('Enter the name of a contact ')
                contact_number = input('Enter the number of a contact ')
                while not Contact.check_phone(contact_number):
                    print('Your phone number is invalid')
                    contact_number = input('Enter the number of a contact ')
                contact_email = input('Enter e-mail address of a contact ')
                while not Contact.check_email(contact_email):
                    print('Your email is invalid')
                    contact_email = input('Enter e-mail address of a contact ')
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
            else:
                print('Enter the correct number')