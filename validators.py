"""Input validation helpers for the Contact Book App."""

import re

EMAIL_PATTERN = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')


def validate_name(name):
    """A name must be non-empty and not just whitespace."""
    if not name or not name.strip():
        return False, 'Name cannot be empty.'
    return True, ''


def validate_age(age_str):
    """Age must be a whole number between 0 and 120."""
    if not age_str.isdigit():
        return False, 'Age must be a whole number (e.g. 21).'
    age = int(age_str)
    if age < 0 or age > 120:
        return False, 'Age must be between 0 and 120.'
    return True, ''


def validate_email(email):
    """Basic email format check: something@something.something"""
    if not EMAIL_PATTERN.match(email):
        return False, 'Email format looks invalid (expected e.g. name@example.com).'
    return True, ''


def validate_mobile(mobile):
    """Mobile number must be exactly 10 digits."""
    if not mobile.isdigit() or len(mobile) != 10:
        return False, 'Mobile number must be exactly 10 digits.'
    return True, ''
