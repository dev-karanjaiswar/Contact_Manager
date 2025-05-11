from file_manager import save_contact, load_contact
contacts = load_contact()

def add_contact(name, number):
    if name in contacts:
        if contacts[name] == number:
            print(f"{name} with the number {number} already exists.")
        else:
            update = input(f"{name} already exists. Do you want to update the number? (yes/no): ").strip().lower()
            if update == "yes":
                contacts[name] = number
                print(f"{name}'s number updated.")
    else:
        if number in contacts.values():
            confirm = input(f"Number {number} already exists under another name. Still add? (yes/no): ").strip().lower()
            if confirm != "yes":
                return
        contacts[name] = number
        print(f"{name} added successfully.")
    save_contact(contacts)

def remove_contact(name):
    if name in contacts:
        contacts.pop(name)
        print(f"{name} removed.")
        save_contact(contacts)
    else:
        print(f"{name} not found.")

def edit_contact(name, number):
    if name in contacts:
        contacts[name] = number
        print(f"{name}'s number updated.")
    else:
        add = input(f"{name} not found. Add as new? (yes/no): ").strip().lower()
        if add == "yes":
            contacts[name] = number
            print(f"{name} added.")
    save_contact(contacts)

def main_menu():
    while True:
        print("\n--- Personal Contact Book ---")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Edit Contact")
        print("4. View All Contacts")
        print("5. Exit")

        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            name = input("Enter name: ").strip()
            number = input("Enter number: ").strip()
            if number.isdigit():
                add_contact(name, int(number))
            else:
                print("Invalid number.")
        elif choice == "2":
            name = input("Enter name to remove: ").strip()
            remove_contact(name)
        elif choice == "3":
            name = input("Enter name to edit: ").strip()
            number = input("Enter new number: ").strip()
            if number.isdigit():
                edit_contact(name, int(number))
            else:
                print("Invalid number.")
        elif choice == "4":
            print("Current Contacts:")
            with open(r"C:\Users\Karan\Desktop\python_practice\Contact_manager\contactbook.txt",'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        name, number = line.split(":")
                        print(f"{name}:{number}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

main_menu()
