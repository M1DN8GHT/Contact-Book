import tkinter as tk
from tkinter import filedialog, messagebox
import csv

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book App")
        self.contact_book_file = None

        # Create menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New Contact Book", command=self.create_contact_book)
        self.file_menu.add_command(label="Open Contact Book", command=self.open_contact_book)

        # Create frames
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.name_label = tk.Label(self.frame, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.pack()
        self.phone_label = tk.Label(self.frame, text="Phone Number:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(self.frame)
        self.phone_entry.pack()
        self.write_button = tk.Button(self.frame, text="Write to Contact Book", command=self.write_to_contact_book)
        self.write_button.pack()
        self.append_button = tk.Button(self.frame, text="Append to Contact Book", command=self.append_to_contact_book)
        self.append_button.pack()

    def create_contact_book(self):
        # Create a new contact book file
        self.contact_book_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if self.contact_book_file:
            with open(self.contact_book_file, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Phone Number"])

    def open_contact_book(self):
        # Open an existing contact book file
        self.contact_book_file = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if self.contact_book_file:
            with open(self.contact_book_file, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)

    def write_to_contact_book(self):
        # Write to the contact book file
        if self.contact_book_file:
            with open(self.contact_book_file, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([self.name_entry.get(), self.phone_entry.get()])
            messagebox.showinfo("Success", "Contact written to contact book")
        else:
            messagebox.showerror("Error", "No contact book file selected")

    def append_to_contact_book(self):
        # Append to the contact book file
        if self.contact_book_file:
            with open(self.contact_book_file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([self.name_entry.get(), self.phone_entry.get()])
            messagebox.showinfo("Success", "Contact appended to contact book")
        else:
            messagebox.showerror("Error", "No contact book file selected")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()