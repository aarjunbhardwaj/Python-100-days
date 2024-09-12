from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# Function to generate a random password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.delete(0, END)  # Clear the password entry field before inserting a new password
    password_entry.insert(0, password)

# Function to save the data to a file
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(password) == 0 or len(website) == 0:
        messagebox.showwarning(title="Empty Fields", message="Please don't leave any empty fields")
    elif messagebox.askokcancel(title=website, message=f"You've entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?"):
        with open("data.txt", mode="a") as file:
            file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# Setting up the GUI window
window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)

# Canvas for logo
canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")  
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "bhardwaj@email.com")
password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
