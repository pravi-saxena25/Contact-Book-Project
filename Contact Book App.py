Contact Book App

A simple command-line Contact Book application built in Python. It lets you create, view, update, delete, search, and count contacts, all stored in memory using a Python dictionary.

Features
Create Contact – Add a new contact with name, age, email, and mobile number.
View Contact – Look up and display details of a specific contact.
Update Contact – Edit the age, email, or mobile number of an existing contact.
Delete Contact – Remove a contact from the contact book.
Search Contact – Search contacts by partial or full name (case-insensitive).
Count Contact – Display the total number of saved contacts.
Exit – Close the application.
Requirements
Python 3.x
No external libraries required (uses only Python's built-in features)
How to Run
Make sure Python 3 is installed on your system.
Save the script as contact_book.py.
Open a terminal in the project folder and run:
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

Contacts are stored in a dictionary where each key is the contact's name and the value is another dictionary holding their details:

python
contacts = {
    "John": {"age": 25, "email": "john@example.com", "mobile": "9876543210"}
}
Project Structure
contact-book-app/
│
├── contact_book.py   # Main application script
└── README.md          # Project documentation
Known Limitations / Notes
Contacts are stored only in memory — all data is lost when the program exits (no file or database persistence yet).
The View, Update, and Search options currently reference variables (age, email, mobile) that need to be pulled from the contact dictionary rather than used directly, so these sections may need a small fix before running smoothly.
Contact names are case-sensitive when used as dictionary keys, though Search is case-insensitive.
Future Improvements
Add persistent storage (e.g., save/load contacts to a JSON or CSV file).
Add input validation (e.g., ensure age is numeric, mobile number format is valid).
Add an "Update" flow that lets users edit only specific fields instead of re-entering all details.
Author

VIT Bhopal – Bioinformatics, Vityarthi Project

License

This project is for academic/educational purposes.