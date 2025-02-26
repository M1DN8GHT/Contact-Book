import tkinter as tk
import os
from tkinter import messagebox
while option != "4":
    print("Select an option: \n1. Read \n2. Write \n3. Append \n4. Exit")
    option = input(">> ")

    if option == "1":
        f = open("story.txt", "r")
        print(f.read())
    elif option == "2":
        f = open("story.txt", "w")
        print("Write Mode:")
        f.write(input(">> "))
        f.write("\n")
    elif option == "3":
        f = open("story.txt", "a")
        print("Append Mode:")
        f.write(input(">> "))
        f.write("\n")
    elif option == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option")
    
    input("Press any key to continue...")
    os.system("cls" if os.name == "nt" else "clear")


f.close()
quit()
