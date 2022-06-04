from tabulate import tabulate
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
        self.list_contact.pop(delete - 1)
        print('The contact was removed')