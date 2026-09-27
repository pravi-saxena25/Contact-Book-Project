# Contact Book App
A simple command-line contact book I built in Python for my VITyarthi project. It lets you add, view, update, delete, search, and count contacts, and everything is saved to a file so you don't lose your data every time you close the program.

## What it does
I wanted something that could handle the basic things a real contact manager needs to do, without overcomplicating it with a database or a GUI. So this app runs in the terminal and gives you a simple menu to work with. Every contact has a name, age, email, and mobile number, and you can do all the usual CRUD stuff (Create, Read, Update, Delete) plus search by name and check how many contacts you've saved.

## Features
- **Create a contact** – enter a name, age, email, and mobile number. If the name already exists, it won't let you overwrite it.
- **View a contact** – look up someone by name and see their full details.
- **Update a contact** – change the age, email, or mobile number for someone already saved.
- **Delete a contact** – remove someone from the list.
- **Search** – find contacts by typing part of a name (not case-sensitive).
- **Count** – see how many contacts you currently have.
- **Data actually sticks around** – contacts are saved to a `contacts.json` file automatically, so they're still there the next time you run the program.
- **Basic input checks** – age has to be a real number, email needs to look like an email, and mobile numbers need to be 10 digits. If you type something wrong, it tells you and asks again instead of just crashing or saving garbage data.

## Built with
- Python 3.x
- Just the standard library — `json` for saving data, `os` for file checks, `re` for the email check. No third-party packages needed.
- A `Contact` class to keep the data organized instead of loose dictionaries everywhere.

## How to run it
You just need Python 3 installed. Check with:

```bash
python --version
```
Then download/clone the project, open a terminal in that folder, and run:

```bash
python main.py
```
That's it — the menu shows up and you take it from there. The first time you add a contact, a `contacts.json` file will show up in the folder on its own; that's just where your data lives.

## Menu
```
1. Create contact
2. View contact
3. Update contact
4. Delete contact
5. Search contact
6. Count contact
7. Exit
```

## How I tested it
I went through each option manually a few times to make sure it behaves the way it should:

- Creating the same name twice → it correctly says the contact already exists instead of overwriting it.
- Typing letters for age, a broken email, or a 5-digit mobile number → all get rejected with a message, and it asks again instead of moving on.
- Viewing a contact that doesn't exist → shows "Contact not found!" instead of erroring out.
- Updating someone and then viewing them again → the new details actually show up.
- Deleting someone and then searching/viewing them → they're gone.
- Searching with just part of a name (like "jo" for "John") → still finds them.
- Closing the program and reopening it → the contacts I added earlier are still there, loaded from the JSON file.

## Project files
```
contact-book-app/
│
├── main.py               # where the program actually starts
├── contact.py             # the Contact class (just holds a person's data)
├── contact_manager.py     # all the create/view/update/delete/search/count logic
├── storage.py              # reads and writes contacts.json
├── validators.py           # checks age/email/mobile before saving
├── contacts.json           # your saved contacts (shows up after first run)
├── README.md               # this file
└── statement.md            # problem statement / scope / who this is for
```

I split it into these separate files instead of one big script so each piece only does one job — makes it a lot easier to read and change later.

## What it doesn't do (yet)
- It's single-user and stored locally only — no accounts, no cloud sync.
- No automated tests yet, everything above was tested by hand.
- Update only lets you re-enter all three fields at once, not just the one you want to change.

## What I'd add if I kept working on it
- Proper unit tests with `pytest` for the manager and validator functions
- CSV export/import so contacts can be moved in and out easily
- Letting update change just one field instead of asking for everything again

## Author
VIT Bhopal – Bioinformatics, Vityarthi Project

## License
This project is for academic/educational purposes.