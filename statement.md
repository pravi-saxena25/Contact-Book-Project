# Problem Statement

I chose this project because when it comes to managing contacts with paper and pencil, remembering and remembering them, or having them in your head, it's not very fun and it's easy to lose them. No there is not a simple, lightweight solution for a person that simply wants to store, search, edit and manage a few contacts without having to drag in a complete CRM or a spreadsheet. So I made a micro-sized command line contact book that does just that, and saves it all to a file so that it really exists the next time you open the book.

# Scope of the Project

This is an application that operates in a console environment, and has been built in Python and for a single user who is managing their own contacts. What it covers:

- Creating new contacts (Name, age, email, mobile number)
The ability to view, edit, and delete contacts
Partial or full name searching -
The next step will be counting how many contacts you have saved.
- Saving all to a local JSON file, thus saving across program close/reopen

What it doesn't do: No GUI, no support for multiple users, no cloud syncing, no integration with something like Google Contacts. These are things that I think I would want to add at a later point but not a part of this project.

# Who this is for

- Users who wish to keep track of classmates, professors, or project team without installing anything heavy.
- Students who are new to Python and are curious about how CRUD operations and file-based storage really work together in an actual (albeit small) application
- Someone who prefers to type some commands in a terminal rather than using a fat contact-management application

The actual function of it (high level).

Add a contact with name, age, email and mobile number — won't allow you to make a duplicate entry.
Click on 2. View a contact — to show someone's full details by typing in their name.
3. Edit a contact — modify the contact's age, email address or mobile number.
4. Remove a contact totally.
5. Search — locate contacts even when you can only remember a portion of the name.
6. **Count** — see how many contacts you have listed at the moment.
8. **Data that remains persistent** — all data is automatically saved to contacts.json, so there's no loss if you close the program.