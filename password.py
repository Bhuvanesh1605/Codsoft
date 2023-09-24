import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            raise ValueError("Password length must be a positive integer.")

        username = username_entry.get()
        if not username:
            raise ValueError("Username cannot be empty.")

        # Generate a random password
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(password_characters) for i in range(password_length))

        # Display the password
        password_label.config(text="Generated Password: " + password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))


# Create the main window
root = tk.Tk()
root.geometry('800x400+50+50')
root.title("Password Generator")
root.configure(bg='lightblue')

# Create labels, entry fields, and buttons
length_label = tk.Label(root, text="Enter Password Length:", font=("Arial", 14, "bold"), bg='lightblue')
length_label.place(x=10, y=80)
length_entry = tk.Entry(root, font=("Arial", 14), width=5)
length_entry.place(x=250, y=80)

username_label = tk.Label(root, text="Enter Username:", font=("Arial", 14, "bold"), bg='lightblue')
username_label.place(x=10, y=130)
username_entry = tk.Entry(root, font=("Arial", 14), width=30)
username_entry.place(x=250, y=130)

generate_button = tk.Button(root, text="Generate Password", font=("Arial", 14), command=generate_password)
generate_button.place(x=250, y=180)

password_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg='lightblue', fg='blue')
password_label.place(x=10, y=250)

# Start the tkinter main loop
root.mainloop()




