class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def __iter__(self):
        return AddressBookIterator(self.contacts)


class AddressBookIterator:
    def __init__(self, contacts):
        self.contacts = contacts
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.contacts):
            contact = self.contacts[self.index]
            self.index += 1
            return contact
        raise StopIteration