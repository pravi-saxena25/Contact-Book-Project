Specifies the Contact data model that is used throughout the app.

class Contact:
    Represents a single contact with name, age, email and mobile number.

    def __init__(self, name, age, email, mobile):
        self.name = name
        self.age = age
        self.email = email
        self.mobile = mobile

    def to_dict(self):
        """Make this contact a plain dict (for JSON storage)."""
        return {
            'age': self.age,
            'email': self.email,
            'mobile': self.mobile
        }

    @staticmethod
    def from_dict(name, data):
        Create a Contact object based on a stored dict.
        return Contact(
            name=name,
            age=data.get('age'),
            email=data.get('email'),
            mobile=data.get('mobile')
        )

    def __str__(self):
        return (f'Name: {self.name}\n'
                f'Age: {self.age}\n'
                f'Mobile Number: {self.mobile}\n'
                f'Email: {self.email}')