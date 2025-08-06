contact_book = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact_book[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print(f"✅ Contact '{name}' added successfully!")

def view_contacts():
    if not contact_book:
        print("📭 Contact book is empty.")
    else:
        print("\n📇 Contact List:")
        for name, details in contact_book.items():
            print(f"\nName: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")

def search_contact():
    search = input("Enter name or phone to search: ")
    found = False
    for name, details in contact_book.items():
        if search == name or search == details["Phone"]:
            print(f"\n🔍 Found Contact:\nName: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            found = True
            break
    if not found:
        print("❌ Contact not found.")

def update_contact():
    name = input("Enter contact name to update: ")
    if name in contact_book:
        print("Enter new details:")
        phone = input("New Phone: ")
        email = input("New Email: ")
        address = input("New Address: ")
        contact_book[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print(f"✅ Contact '{name}' updated successfully.")
    else:
        print("❌ Contact not found.")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"🗑 Contact '{name}' deleted.")
    else:
        print("❌ Contact not found.")

def menu():
    while True:
        print("\n📱 Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

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
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Please select from 1-6.")

# Run the contact book
menu()
