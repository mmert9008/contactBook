def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

def add_contact(contact_book):
    name = input()
    phone = input()
    email = input()
    address = input()

    if name in contact_book.keys():
        print("Contact already exists!")
    else:
        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")

def view_contact(contact_book):
    name = input()
    if name not in contact_book.keys():
        print("Contact not found!")
    else:
        print(f"Name: {name}\nPhone: {contact_book[name]['phone']}\nEmail: {contact_book[name]['email']}\nAddress: {contact_book[name]['address']}")

def edit_contact(contact_book):
    name = input()
    if name not in contact_book.keys():
        print("Contact not found!")
    else:
        contact_book[name] = {
            "phone": input(),
            "email": input(),
            "address": input()
        }
        print("Contact updated successfully!")

def delete_contact(contact_book):
    name = input()
    if name not in contact_book.keys():
        print("Contact not found!")
    else:
        del contact_book[name]
        print("Contact deleted successfully!")





if __name__ == "__main__":
    contact_book = {}

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            view_contact(contact_book)
        elif choice == '3':
            edit_contact(contact_book)
        elif choice == '4':
            delete_contact(contact_book)
#        elif choice == '5':
#            list_all_contacts(contact_book)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
