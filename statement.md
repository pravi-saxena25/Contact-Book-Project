# Problem Statement

I picked this project because keeping track of contacts manually — scattered notes, a phone that could get lost, or just remembering things in your head — is a pain and things fall through the cracks. There isn't really a simple, lightweight option for someone who just wants to store, look up, update, and organize a handful of contacts without dragging in a full CRM or a spreadsheet. So I built a small command-line contact book that does exactly that, and saves everything to a file so it's actually there the next time you open it.

# Scope of the Project

This is a console-based Python app meant for one person managing their own contacts. What it covers:

- Adding new contacts (name, age, email, mobile number)
- Viewing, updating, and deleting contacts
- Searching by partial or full name
- Counting how many contacts you've saved
- Saving everything to a local JSON file so it survives closing/reopening the program

What it doesn't cover: there's no GUI, no support for multiple users, no cloud syncing, and no integration with something like Google Contacts. Those are things I'd consider adding later, but they were out of scope for this project.

# Who this is for

- Students who just want a simple way to keep track of classmates, professors, or project teammates without installing anything heavy
- Beginners learning Python who want to see how CRUD operations and file-based storage actually work together in a real (if small) project
- Anyone who'd rather type a few commands in a terminal than click through a bloated contact-management app

# What it actually does (high level)

1. **Create a contact** — add someone new with their name, age, email, and mobile number; won't let you accidentally create a duplicate.
2. **View a contact** — pull up someone's full details by typing their name.
3. **Update a contact** — change the age, email, or mobile number for someone already in there.
4. **Delete a contact** — remove someone for good.
5. **Search** — find contacts even if you only remember part of their name.
6. **Count** — check how many contacts you've got saved right now.
7. **Data that sticks around** — everything gets written to `contacts.json` automatically, so nothing is lost when you close the program.
