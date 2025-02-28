import tkinter as tk
import os
import csv
from tkinter import messagebox

# Ensure both contact books exist
for filename in ["contacts1.csv", "contacts2.csv"]:
    try:
        with open(filename, "x", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Phone", "Email"])  # Write header
    except FileExistsError:
        pass

option = ""
# This code gives the user a choice to read, write, append, or exit a contact book.
while option != "4":
    print("Select an option: \n1. Read \n2. Write \n3. Append \n4. Exit")
    option = input(">> ")

    if option in ["1", "2", "3"]:
        book_choice = input("Which contact book do you want to use (1 or 2): ")
        if book_choice == "1":
            filename = "contacts1.csv"
        elif book_choice == "2":
            filename = "contacts2.csv"
        else:
            print("Invalid contact book selected.")
            continue
# This code shows what happens after picking one of the options.
    if option == "1":
        try:
            with open(filename, "r", newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    print(", ".join(row))
        except FileNotFoundError:
            print("The file does not exist.")
    elif option == "2":
        with open(filename, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Phone", "Email"])  # Write header
            print("Write Mode:")
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            writer.writerow([name, phone, email])
    elif option == "3":
        with open(filename, "a", newline='') as f:
            writer = csv.writer(f)
            print("Append Mode:")
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            writer.writerow([name, phone, email])
    elif option == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option")
    
    input("Press any key to continue...")
    os.system("cls" if os.name == "nt" else "clear")

quit()


