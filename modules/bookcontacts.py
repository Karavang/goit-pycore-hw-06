from collections import UserDict


class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):

    def __init__(self, value):
        super().__init__(value)
        self.name = value[1]

    def getName(self):
        return self.name

    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.phone = value[2]
        if len(self.phone) == 10 and self.phone.isdigit():
            return self.phone
        else:
            raise ValueError("Invalid phone")

    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone):
        self.phones.append(str(phone))
    def remove_phone(self,phone):
        if phone in self.phones:
            del self.phones[phone]
    def edit_phone(self,phone,new_phone):
        if phone in self.phones:
            self.phones[phone] = new_phone
    def find_phone(self,phone):
        if phone in self.phones:
            return "this phone in phones"
        else:
            return "lib doesn`t contain this phone"
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    data = {}

    def add_record(self):
        self.data(self["name"]) = Phone(self["phone"])

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return "deleted"
        else:
            return "contact not found"

    pass
