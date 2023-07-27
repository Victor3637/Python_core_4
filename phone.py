
from field import Field

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    @Field.value.setter
    def value(self, new_value):
        if not self.is_valid_phone(new_value):
            raise ValueError("Invalid phone number")
        self._value = new_value

    @staticmethod
    def is_valid_phone(phone):
        # Add your validation logic for the phone number if needed
        return True

    def __repr__(self):
        return self._value  # Return the phone number as a string
