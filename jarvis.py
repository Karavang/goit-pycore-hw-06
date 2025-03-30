from modules.parse_input import parse_input
from modules.add_contant import add_contact
from modules.change_contact import change_contact
from modules.show_phone import show_phone
from modules.decocatcher import input_error


import os


def main():
    contacts = {}
    while True:
        command = input("Enter a command: ")
        parsed = parse_input(command)
        match parsed[0]:
            case "hello":
                print("How can I help you?")
            case "add":
                print(input_error(add_contact)(parsed, contacts))
            case "change":
                print(input_error(change_contact)(parsed, contacts))
            case "phone":
                print(input_error(show_phone)(parsed, contacts))
            case "all":
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")

            case "close" | "exit":
                try:
                    print("Good bye!")
                    # os.system('pkill -f "code"')
                    break
                except:
                    print("Failed to close the window")
            case _:
                print("Unknown command")


if __name__ == "__main__":
    main()
