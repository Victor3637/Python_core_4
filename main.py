from address_book import AddressBook
from record import Record
from phone import Phone
from birthday import Birthday

if __name__ == "__main__":
    address_book = AddressBook()

    # Додавання контактів
    contact1 = Record("John", Phone("+1234567890"))
    contact2 = Record("Alice", Phone("+9876543210"), Birthday("1990-05-25"))
    address_book.add_contact(contact1)
    address_book.add_contact(contact2)

    # Перевірка кількості днів до наступного дня народження
    for contact in address_book:
        print(contact)
        if contact.birthday:
            days_left = contact.days_to_birthday()
            print(f"Days to birthday: {days_left}")

    # Приклад встановлення нового значення номера телефону
    contact1.value.value = "+1111111111"

    # Приклад встановлення нового значення дня народження
    contact2.value.value = "1990-06-30"