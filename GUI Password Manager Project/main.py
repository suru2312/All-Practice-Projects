from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

FONT_NAME = "Courier"
# ---------------------------- SEARCH PASSWORDS ------------------------------- #
def search():
    website = website_input.get()
    try:
        with open("password_db.json", "r") as pwd_db:
            data = json.load(pwd_db)
    except FileNotFoundError:
        messagebox.showerror(title = "Error", message = "No Data File Found.")
    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="Data file is empty or corrupted.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title = website,
                message = f"Email : {email}\nPassword : {password}"
            )
        else:
            messagebox.showwarning(
                title = "Not Found",
                message = f"No details for {website} exist."
            )

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
    
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    
    if len(website) > 0 and len(email) > 0 and len(password) > 0:
        
        try:
            with open("password_db.json", "r") as pwd_db:
                data = json.load(pwd_db)
        
        except FileNotFoundError:
            with open("password_db.json", "w") as pwd_db:
                json.dump(new_data, pwd_db, indent=4)
        
        except json.JSONDecodeError:
            # File exists but is empty/corrupted
            data = {}
            data.update(new_data)
            with open("password_db.json", "w") as pwd_db:
                json.dump(data, pwd_db, indent=4)
        
        else:
            data.update(new_data)
            with open("password_db.json", "w") as pwd_db:
                json.dump(data, pwd_db, indent=4)
        
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
    
    else:
        messagebox.showwarning(title="Warning", message="You can't leave any box empty!")

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
website_input = Entry(width = 33)
website_input.grid(column=1, row=1, padx=5, pady=5, sticky="w")
website_input.focus()
email_input = Entry(width = 55)
email_input.grid(column=1, row=2, columnspan=2, padx=5, pady=5, sticky="w")
email_input.insert(0, "surajsharma23122001@gmail.com")
password_input = Entry(width = 33)
password_input.grid(column = 1, row = 3, padx=5, pady=5, sticky="w")


# Buttons
search_button = Button(text = "Search", command = search, width = 16)
search_button.grid(column = 2, row = 1, padx=5, pady=5, sticky="w")
generate_password_button = Button(text = "Generate Password", command = generate_password, width = 16)
generate_password_button.grid(column = 2, row = 3, padx=5, pady=5, sticky="w")
add_button = Button(text = "Add to Database", command = save_password, width = 47)
add_button.grid(column = 1, row = 4, columnspan = 2, padx=5, pady=5, sticky="w")


window.mainloop()