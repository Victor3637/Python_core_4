from datetime import datetime

class Record:
    def __init__(self, name, value, birthday=None):
        self.name = name
        self.value = value
        self.birthday = birthday

    def days_to_birthday(self):
        if not self.birthday:
            return None

        today = datetime.now()
        next_birthday = datetime(today.year, self.birthday.get_month(), self.birthday.get_day())
        if today > next_birthday:
            next_birthday = datetime(today.year + 1, self.birthday.get_month(), self.birthday.get_day())

        days_until_birthday = (next_birthday - today).days
        return days_until_birthday

    def __repr__(self):
        return f"{self.name}: {self.value}"