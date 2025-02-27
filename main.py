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

while option != "4":
    print("Select an option: \n1. Read \n2. Write \n3. Append \n4. Exit")
    option = input(">> ")

    if option in ["1", "2", "3"]:
        filename = input("Which contact book do you want to use (contacts1.csv or contacts2.csv): ")
        if filename not in ["contacts1.csv", "contacts2.csv"]:
            print("Invalid contact book selected.")
            continue

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


