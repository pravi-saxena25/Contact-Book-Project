"""Core business logic: create, view, update, delete, search, and count contacts."""

from contact import Contact
from validators import validate_name, validate_age, validate_email, validate_mobile

class ContactManager:
    """Manages the in-memory contact dictionary and keeps it in sync with storage."""

    def __init__(self, storage):
        self.storage = storage
        self.contacts = self.storage.load()

    def _prompt_valid(self, prompt_text, validator):
        """Keep asking until the user enters something that passes the validator."""
        while True:
            value = input(prompt_text)
            is_valid, error_message = validator(value)
            if is_valid:
                return value
            print(f'Invalid input: {error_message}')

    def create_contact(self):
        name = input('Enter your name = ')
        is_valid, error_message = validate_name(name)
        if not is_valid:
            print(f'Invalid input: {error_message}')
            return

        if name in self.contacts:
            print(f'Contact name {name} already exists!')
            return

        age = self._prompt_valid('Enter age = ', validate_age)
        email = self._prompt_valid('Enter email = ', validate_email)
        mobile = self._prompt_valid('Enter mobile number = ', validate_mobile)

        contact = Contact(name, int(age), email, mobile)
        self.contacts[name] = contact.to_dict()
        self.storage.save(self.contacts)
        print(f'Contact name {name} has been created successfully!')

    def view_contact(self):
        name = input('Enter contact name to view = ')
        if name in self.contacts:
            contact = Contact.from_dict(name, self.contacts[name])
            print(contact)
        else:
            print('Contact not found!')

    def update_contact(self):
        name = input('Enter contact name to update = ')
        if name not in self.contacts:
            print('Contact not found!')
            return

        age = self._prompt_valid('Enter updated age = ', validate_age)
        email = self._prompt_valid('Enter updated email = ', validate_email)
        mobile = self._prompt_valid('Enter updated mobile number = ', validate_mobile)

        contact = Contact(name, int(age), email, mobile)
        self.contacts[name] = contact.to_dict()
        self.storage.save(self.contacts)
        print(f'Contact {name} has been updated successfully!')

    def delete_contact(self):
        name = input('Enter contact name to delete = ')
        if name in self.contacts:
            del self.contacts[name]
            self.storage.save(self.contacts)
            print(f'Contact name {name} has been deleted successfully!')
        else:
            print('Contact not found!')

    def search_contact(self):
        search_name = input('Enter contact name to search = ')
        found = False

        for name, data in self.contacts.items():
            if search_name.lower() in name.lower():
                contact = Contact.from_dict(name, data)
                print(
                    f'Found - Name: {contact.name}, '
                    f'Age: {contact.age}, '
                    f'Mobile Number: {contact.mobile}, '
                    f'Email: {contact.email}'
                )
                found = True

        if not found:
            print('No contact found with that name')

    def count_contacts(self):
        print(f'Total contacts in your book: {len(self.contacts)}')

    def run(self):
        """Main menu loop."""
        while True:
            print('\nContact Book App')
            print('1. Create contact')
            print('2. View contact')
            print('3. Update contact')
            print('4. Delete contact')
            print('5. Search contact')
            print('6. Count contact')
            print('7. Exit')

            choice = input('Enter your choice = ')

            if choice == '1':
                self.create_contact()
            elif choice == '2':
                self.view_contact()
            elif choice == '3':
                self.update_contact()
            elif choice == '4':
                self.delete_contact()
            elif choice == '5':
                self.search_contact()
            elif choice == '6':
                self.count_contacts()
            elif choice == '7':
                print('Goodbye... Closing the program')
                break
            else:
                print('Invalid input')
