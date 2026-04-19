import requests
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# -------------------- CONFIG -------------------- #
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = "graph1"

BASE_URL = "https://pixe.la/v1/users"
PIXEL_ENDPOINT = f"{BASE_URL}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"

HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# -------------------- FUNCTIONS -------------------- #

def add_pixel():
    date = date_entry.get()
    quantity = quantity_entry.get()

    data = {
        "date": date,
        "quantity": quantity
    }

    try:
        response = requests.post(PIXEL_ENDPOINT, json=data, headers=HEADERS)
        response.raise_for_status()
        messagebox.showinfo("Success", "Pixel added successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def update_pixel():
    date = date_entry.get()
    quantity = quantity_entry.get()

    url = f"{PIXEL_ENDPOINT}/{date}"

    data = {
        "quantity": quantity
    }

    try:
        response = requests.put(url, json=data, headers=HEADERS)
        response.raise_for_status()
        messagebox.showinfo("Success", "Pixel updated!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_pixel():
    date = date_entry.get()
    url = f"{PIXEL_ENDPOINT}/{date}"

    try:
        response = requests.delete(url, headers=HEADERS)
        response.raise_for_status()
        messagebox.showinfo("Success", "Pixel deleted!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def set_today():
    today = datetime.now().strftime("%Y%m%d")
    date_entry.delete(0, END)
    date_entry.insert(0, today)


# -------------------- UI -------------------- #

window = Tk()
window.title("Pixela Tracker")
window.config(padx=30, pady=30)

# Labels
Label(text="Date (YYYYMMDD):").grid(row=0, column=0, sticky="e")
Label(text="Quantity:").grid(row=1, column=0, sticky="e")

# Inputs
date_entry = Entry(width=20)
date_entry.grid(row=0, column=1)

quantity_entry = Entry(width=20)
quantity_entry.grid(row=1, column=1)

# Buttons
Button(text="Set Today", command=set_today).grid(row=0, column=2, padx=5)

Button(text="Add Pixel", width=20, command=add_pixel).grid(row=2, column=0, columnspan=3, pady=5)
Button(text="Update Pixel", width=20, command=update_pixel).grid(row=3, column=0, columnspan=3, pady=5)
Button(text="Delete Pixel", width=20, command=delete_pixel).grid(row=4, column=0, columnspan=3, pady=5)

window.mainloop()