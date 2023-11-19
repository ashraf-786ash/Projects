class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
        self.contacts.append(contact)
        print(f"\nContact '{name}' added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("\nContact list is empty.")
        else:
            print("\nContact List:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}")

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
                results.append(contact)
        return results

    def update_contact(self, index, name, phone, email, address):
        self.contacts[index]['name'] = name
        self.contacts[index]['phone'] = phone
        self.contacts[index]['email'] = email
        self.contacts[index]['address'] = address
        print("\nContact updated successfully!")

    def delete_contact(self, index):
        deleted_name = self.contacts[index]['name']
        del self.contacts[index]
        print(f"\nContact '{deleted_name}' deleted successfully!")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            address = input("Enter the address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contact_list()

        elif choice == '3':
            keyword = input("Enter the name or phone number to search: ")
            search_results = contact_book.search_contact(keyword)

            if search_results:
                print("\nSearch Results:")
                for contact in search_results:
                    print(f"Name: {contact['name']}, Phone: {contact['phone']}")
            else:
                print("\nNo matching contacts found.")

        elif choice == '4':
            index = int(input("Enter the index of the contact to update: ")) - 1
            if 0 <= index < len(contact_book.contacts):
                name = input("Enter the updated name: ")
                phone = input("Enter the updated phone number: ")
                email = input("Enter the updated email address: ")
                address = input("Enter the updated address: ")
                contact_book.update_contact(index, name, phone, email, address)
            else:
                print("Invalid index. Please enter a valid index.")

        elif choice == '5':
            index = int(input("Enter the index of the contact to delete: ")) - 1
            if 0 <= index < len(contact_book.contacts):
                contact_book.delete_contact(index)
            else:
                print("Invalid index. Please enter a valid index.")

        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
