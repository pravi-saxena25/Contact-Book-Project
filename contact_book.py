# Empty dictionary
contacts = {}

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

    # Create contact
    if choice == '1':
        name = input('Enter your name = ')

        if name in contacts:
            print(f'Contact name {name} already exists!')
        else:
            age = input('Enter age = ')
            email = input('Enter email = ')
            mobile = input('Enter mobile number = ')

            contacts[name] = {
                'age': int(age),
                'email': email,
                'mobile': mobile
            }

            print(f'Contact name {name} has been created successfully!')

    # View contact
    elif choice == '2':
        name = input('Enter contact name to view = ')

        if name in contacts:
            contact = contacts[name]

            print(f'Name: {name}')
            print(f'Age: {contact["age"]}')
            print(f'Mobile Number: {contact["mobile"]}')
            print(f'Email: {contact["email"]}')
        else:
            print('Contact not found!')

    # Update contact
    elif choice == '3':
        name = input('Enter contact name to update = ')

        if name in contacts:
            age = input('Enter updated age = ')
            email = input('Enter updated email = ')
            mobile = input('Enter updated mobile number = ')

            contacts[name] = {
                'age': int(age),
                'email': email,
                'mobile': mobile
            }

            print(f'Contact {name} has been updated successfully!')
        else:
            print('Contact not found!')

    # Delete contact
    elif choice == '4':
        name = input('Enter contact name to delete = ')

        if name in contacts:
            del contacts[name]
            print(f'Contact name {name} has been deleted successfully!')
        else:
            print('Contact not found!')

    # Search contact
    elif choice == '5':
        search_name = input('Enter contact name to search = ')
        found = False

        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(
                    f'Found - Name: {name}, '
                    f'Age: {contact["age"]}, '
                    f'Mobile Number: {contact["mobile"]}, '
                    f'Email: {contact["email"]}'
                )
                found = True

        if not found:
            print('No contact found with that name')

    # Count contacts
    elif choice == '6':
        print(f'Total contacts in your book: {len(contacts)}')

    # Exit
    elif choice == '7':
        print('Goodbye... Closing the program')
        break

    else:
        print('Invalid input')
