class Contact:
    def __init__(self, contact_name, contact_number):
        self.name = contact_name
        self.number = contact_number

    def show(self):
        print(self.name, ' - ', self.number)

    def match(self, term):
        return term in self.name or term in self.number


class ContactList:
    def __init__(self):
        self.list_contact = []

    def add_to_list(self, contact):
        self.list_contact.append(contact)

    def find(self, term):
        find_list = []
        for i in self.list_contact:
            if i.match(term):
                find_list.append(i)
        if len(find_list) == 0:
            print("You don't have this contact")
        else:
            for i in find_list:
                i.show()

    def print_all(self):
        for i in self.list_contact:
            i.show()


class Dispatcher():
    def __init__(self):
        self.cl = ContactList()
        self.intro()

    def intro(self):
        print("That is your Contact Book. You have next options:\n 1 - add contact\n 2 - find contact\n 3 - receive the whole list of contacts\n 4 - exit the Contact Book\n ")
        while True:
            user_choice = input('Make your choice ')
            if user_choice == '1':
                contact_name = input('Enter the name ')
                contact_number = input('Enter the number of a contact ')
                new_contact = Contact(contact_name, contact_number)
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
            else:
                print('Enter the correct number')


Dispatcher()
