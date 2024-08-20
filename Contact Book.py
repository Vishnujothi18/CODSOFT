# Contact Management System

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter physical address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]

    if not found_contacts:
        print("No contacts found.")
    else:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def update_contact():
    view_contacts()
    index = int(input("Enter the number of the contact you want to update: ")) - 1

    if 0 <= index < len(contacts):
        contact = contacts[index]
        print(f"Updating contact {contact['name']}...")

        contact['name'] = input(f"Enter new name ({contact['name']}): ") or contact['name']
        contact['phone'] = input(f"Enter new phone number ({contact['phone']}): ") or contact['phone']
        contact['email'] = input(f"Enter new email address ({contact['email']}): ") or contact['email']
        contact['address'] = input(f"Enter new physical address ({contact['address']}): ") or contact['address']

        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

def delete_contact():
    view_contacts()
    index = int(input("Enter the number of the contact you want to delete: ")) - 1

    if 0 <= index < len(contacts):
        deleted_contact = contacts.pop(index)
        print(f"Contact {deleted_contact['name']} deleted successfully!")
    else:
        print("Invalid contact number.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
