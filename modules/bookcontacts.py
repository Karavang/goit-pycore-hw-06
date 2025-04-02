from collections import UserDict


class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):

    def __init__(self, value):
        super().__init__(value)
        self.name = value

    def getName(self):
        return self.name

    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if len(self.phone) == 10 and self.phone.isdigit():
            self.phone = value
        else:
            raise ValueError("Invalid phone")

    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, phone, new_phone):
        for p in self.phones:
            if p.value == phone:
                self.phones[phone] = Phone(new_phone)

    def find_phone(self, phone):
        if phone in self.phones:
            return "this phone in phones"
        else:
            return "lib doesn`t contain this phone"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, note: Record):
        self.data[note.name.value] = note

    def find(self, name):
        if name in self.data:
            return self.data.get(name)
        return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return "deleted"
        else:
            return "contact not found"

    pass
