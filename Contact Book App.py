Contact Book App
Python implementation of a very simple contact book application using command line. It allows you to make, display, edit, remove, query, and count contacts in memory, all in the form of a Python dictionary.

Features
Create Contact – Add a new contact with name, age, email and mobile number.
View Contact – Display and view information on a contact.
Update Contact – Edit contact's age, email or mobile number.
Delete Contact – Remove contact from the contact book.
Search Contact – Search for contacts using either a partial or full name (case-insensitive).
Count Contact – Shows the number of contacts saved.
Exit – Close the application.
Requirements
Python 3.x
No external libraries are needed (only Python built-in features are used)
How to Run
Ensure that you have python 3 installed.
Save the script as contact_book.py.
Open terminal window in project folder, and execute:
bash
   python contact_book.py
Follow the on-screen menu to manage your contacts.
Menu Options
1. Create contact
2. View contact
3. Update contact
4. Delete contact
5. Search contact
6. Count contact
7. Exit
Data Structure

Contacts are kept in a dictionary with keys as contact names, and values as dictionaries of contact information:

python
contacts = {
    "John": {"age": 25, "email": "john@example.com", "mobile": "9876543210"}
}
Project Structure
contact-book-app/
│
│   └── contact_book.py - main application script
└── README.md          # Project documentation
Known Limitations / Notes
Contacts are not yet persisted in a file or database (only in memory).
The View, Update and Search are currently using variables that must be retrieved from the contact dictionary as opposed to directly, and so these sections may require some minor tweaking prior to running.
The names of contacts are not case sensitive for the dictionary but they are case sensitive to use as keys.
Future Improvements
Include persistent storage (save / load contacts to a JSON / CSV file).
Include input validation (e.g. Age must be a number, Mobile number must be a valid format).
Include an "Update" flow for users to update only specific fields without having to re-input all fields.
Author

VIT Bhopal – Bioinformatics, Vityarthi Project

License
This project is for academic/educational purposes.