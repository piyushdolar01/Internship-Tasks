contacts = []

def add_contact():
    print("\n Add New Contact")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully!")

def view_contacts():
    print("\n Contact List:")
    if not contacts:
        print("No contact found.")
    else:
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    print("\n Search Contact")
    keyword = input("Enter Name or Phone number to search: ")
    found = False
    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword == contact['phone']:
            print(f"\nName    : {contact['name']}")
            print(f"Phone   : {contact['phone']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    print("\n Update Contact")
    phone = input("Enter phone number of the contact to update: ")
    for contact in contacts:
        if contact['phone'] == phone:
            print("Leave a field blank to keep it unchanged.")
            new_name = input("New Name: ") or contact['name']
            new_email = input("New Email: ") or contact['email']
            new_address = input("New Address: ") or contact['address']
            contact['name'] = new_name
            contact['email'] = new_email
            contact['address'] = new_address
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    print("\n Delete Contact")
    phone = input("Enter phone number of the contact to delete: ")
    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def contact_book():
    while True:
        print("\n----- Contact Book -----")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

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
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

contact_book()
