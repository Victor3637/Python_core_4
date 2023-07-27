from datetime import datetime
from field import Field

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)

    @Field.value.setter
    def value(self, new_value):
        if not self.is_valid_birthday(new_value):
            raise ValueError("Invalid birthday format")
        self._value = new_value

    @staticmethod
    def is_valid_birthday(birthday):
        # Add the necessary validation for the birthday format if needed
        return True

    def get_month(self):
        # Extract the month from the date string
        date_obj = datetime.strptime(self._value, "%Y-%m-%d")
        return date_obj.month

    def get_day(self):
        # Extract the day from the date string
        date_obj = datetime.strptime(self._value, "%Y-%m-%d")
        return date_obj.day
