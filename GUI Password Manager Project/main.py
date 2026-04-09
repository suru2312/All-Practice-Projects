from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    
    is_ok = False
    
    if len(website) > 0 and len(email) > 0 and len(password) > 0:
        is_ok = messagebox.askokcancel(title = website, message = f"These are the details you entered :\nEmail : {email}\nPassword : {password}\nIs it okay to save?")
        if is_ok:
            with open("password_db.txt", "a") as pwd_db:
                pwd_db.write(f"Website : {website} || Email : {email} || Password : {password}\n\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
    else:
        messagebox.showwarning(title = "Warning", message = f"You can't leave any box empty!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

# Canvas Set-Up
canvas = Canvas(width = 200, height = 200)
logo_image = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_image)
canvas.grid(column = 1, row = 0)


# Labels
website_label = Label(text = "Website : ", font = (FONT_NAME, 10, "bold"))
website_label.grid(column=0, row=1, padx=5, pady=5, sticky="e")
email_label = Label(text = "Email/Username : ", font = (FONT_NAME, 10, "bold"))
email_label.grid(column=0, row=2, padx=5, pady=5, sticky="e")
password_label = Label(text = "Password : ", font = (FONT_NAME, 10, "bold"))
password_label.grid(column = 0, row = 3, padx=5, pady=5, sticky="e")


# Input Areas
website_input = Entry(width = 55)
website_input.grid(column=1, row=1, columnspan=2, padx=5, pady=5, sticky="w")
website_input.focus()
email_input = Entry(width = 55)
email_input.grid(column=1, row=2, columnspan=2, padx=5, pady=5, sticky="w")
email_input.insert(0, "surajsharma23122001@gmail.com")
password_input = Entry(width = 33)
password_input.grid(column = 1, row = 3, padx=5, pady=5, sticky="w")


# Buttons
generate_password_button = Button(text = "Generate Password", command = generate_password, width = 16)
generate_password_button.grid(column = 2, row = 3, padx=5, pady=5, sticky="w")
add_button = Button(text = "Add to Database", command = save_password, width = 47)
add_button.grid(column = 1, row = 4, columnspan = 2, padx=5, pady=5, sticky="w")


window.mainloop()