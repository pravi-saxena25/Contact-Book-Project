"""Handles saving and loading contacts to/from a JSON file on disk."""

import json
import os


class JSONStorage:
    """Persists contacts as a JSON file (default: contacts.json)."""

    def __init__(self, filepath='contacts.json'):
        self.filepath = filepath

    def load(self):
        """Load contacts from the JSON file. Returns {} if missing or unreadable."""
        if not os.path.exists(self.filepath):
            return {}
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print('Warning: contacts.json could not be read, starting with an empty contact book.')
            return {}

    def save(self, contacts_dict):
        """Write the contacts dictionary to the JSON file."""
        try:
            with open(self.filepath, 'w') as f:
                json.dump(contacts_dict, f, indent=4)
        except IOError:
            print('Warning: could not save contacts to disk.')
