import os

File_Path = "C:\\Users\\Karan\\Desktop\\python_practice\\Contact_manager\\contactbook.txt"

def load_contact():
    contacts = {}
    if os.path.exists(File_Path):
        with open(File_Path,'r') as file:
            for line in file:
                name, number = line.strip().split(":")
                contacts[name] = int(number)
    return contacts

def save_contact(contacts):
    with open(File_Path,'w') as file:
        for name, number in contacts.items():
            file.write(f"{name}:{number}\n")