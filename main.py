def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")


def add_contact(contact_book):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")

    if name in contact_book.keys():
        print("\nContact already exists!\n")
    else:
        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("\nContact added successfully!\n")


def view_contact(contact_book):
    name = input("Enter the name of the contact to view: ")
    if name not in contact_book.keys():
        print("\nContact not found!\n")
    else:
        print(f"\nName: {name}\nPhone: {contact_book[name]['phone']}\nEmail: {contact_book[name]['email']}\nAddress: {contact_book[name]['address']}\n")


def edit_contact(contact_book):
    name = input("Enter the name of the contact to edit: ")
    if name not in contact_book.keys():
        print("\nContact not found!\n")
    else:
        new_phone = input("Phone: ")
        new_email = input("Email: ")
        new_address = input("Address: ")

        if new_phone:
            contact_book[name]["email"] = new_phone
        if new_email:
            contact_book[name]["email"] = new_email
        if new_address:
            contact_book[name]["address"] = new_address
        print("\nContact updated successfully!\n")


def delete_contact(contact_book):
    name = input("Enter the name of the contact to delete: ")
    if name not in contact_book.keys():
        print("\nContact not found!\n")
    else:
        del contact_book[name]
        print("\nContact deleted successfully!\n")


def list_all_contacts(contact_book):
    if not contact_book:
        print("\nNo contacts available.\n")
    else:
        for key, value in contact_book.items():
            print(f"\nName: {key}\nPhone: {value['phone']}\nEmail: {value['email']}\nAddress: {value['address']}\n")





if __name__ == "__main__":
    contact_book = {}

    while True:
        display_menu()
        choice = input("Please make a selection (1-6): ")

        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            view_contact(contact_book)
        elif choice == '3':
            edit_contact(contact_book)
        elif choice == '4':
            delete_contact(contact_book)
        elif choice == '5':
            list_all_contacts(contact_book)
        elif choice == '6':
            print("\nExiting Contact Book. Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.\n")

