"""Entry point for the Contact Book App."""

from contact_manager import ContactManager
from storage import JSONStorage

def main():
    storage = JSONStorage('contacts.json')
    manager = ContactManager(storage)
    manager.run()

if __name__ == '__main__':
    main()