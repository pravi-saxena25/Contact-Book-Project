# Contact Book App

This is a command-line contact book I built in Python for my VITyarthi project. You can add, view, update, delete, and search contacts, and see how many you've saved. Everything gets written to a file, so nothing disappears when you close the program.

## Why I made it this way

I wanted to build something that covers what a real contact manager does, but without a database or a GUI, since that felt like too much for a first proper project. So it runs in the terminal and shows a simple menu. Each contact has a name, age, email, and mobile number, and the app does all four CRUD operations (create, read, update, delete) plus search by name and a contact count.

## What it can do

You can create a contact by entering the name, age, email, and mobile number. If the name is already saved, the app refuses to overwrite it. To look someone up, you type their name and it prints their details. Updating lets you change the age, email, and mobile number of an existing contact, and deleting removes them completely.

Search works on part of a name and ignores upper/lower case, so typing "jo" will find "John". There's also a count option that tells you how many contacts you have.

Contacts are saved automatically to `contacts.json`, so they're still there the next time you open the app.

I also added basic input checks because I didn't want it crashing or saving junk. Age has to be a number, the email has to look like an email, and the mobile number has to be exactly 10 digits. If something's wrong, it says so and asks again.

## What I used

Just Python 3 and its standard library: `json` for saving data, `os` for checking if the file exists, and `re` for the email check. Nothing needs to be installed. I also made a `Contact` class so the data stays organised instead of passing loose dictionaries around everywhere.

## How to run it

Make sure Python 3 is installed:

```bash
python --version
```

Then download or clone the project, open a terminal in the folder, and run:

```bash
python main.py
```

The menu shows up and you can pick from there. The first time you add a contact, a `contacts.json` file appears in the folder by itself. That's where your data is stored.

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

I don't have automated tests yet, so I tried everything by hand a few times. Adding the same name twice correctly gave me "contact already exists" instead of overwriting the old one. When I typed letters for age, a broken email, or a 5-digit mobile number, it rejected each one and asked again. Viewing a contact that doesn't exist printed "Contact not found!" rather than throwing an error.

I also checked that updating someone and viewing them again showed the new details, and that a deleted contact really was gone from both view and search. Searching with just "jo" still found "John". Finally, I closed the program and reopened it, and the contacts I'd added earlier loaded back from the JSON file.

## Project files

```
contact-book-app/
│
├── main.py               # where the program starts
├── contact.py            # the Contact class (holds one person's data)
├── contact_manager.py    # create/view/update/delete/search/count logic
├── storage.py            # reads and writes contacts.json
├── validators.py         # checks age, email, and mobile before saving
├── contacts.json         # your saved contacts (appears after first run)
├── README.md             # this file
└── statement.md          # problem statement, scope, and target users
```

I split the code across these files instead of writing one long script so each file has one job. It made things easier for me to read and change while I was working on it.

## Limitations

It's a single-user app and everything is stored locally, so there are no accounts or cloud sync. As I said above, all my testing was manual. Also, the update option makes you re-enter all three fields even if you only want to change one, which is a bit annoying.

## What I'd add next

If I kept working on it, I'd start with proper unit tests using `pytest` for the manager and validator functions. After that I'd add CSV import and export so contacts are easy to move around, and fix the update option so it only changes the field you pick.

## Author

Pravi Saxena, VIT Bhopal (VITyarthi project)

## License

This project is for academic and educational purposes.
