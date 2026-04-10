import random
import time
from tkinter import *
from tkinter import messagebox
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = []

try:
    data = pd.read_csv(r"data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv(r"data\french_words.csv")
    to_learn = original_data.to_dict(orient = "records")
else:
    to_learn = data.to_dict(orient = "records")


def next_card():
    global current_card, flip_timer
    if len(to_learn) == 0:
        messagebox.showinfo(title="Done", message="You've learned all words!")
        return
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text = "English")
    canvas.itemconfig(card_word, text = current_card["English"])
    canvas.itemconfig(card_background, image = card_back_image)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv(r"data\words_to_learn.csv", index = False)
    next_card()

# ------------------------- UI Design ------------------------------ #
window = Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)
flip_timer = window.after(3000, func = flip_card)

# Canvas
canvas = Canvas(width = 800, height = 526, highlightthickness = 0, bg = BACKGROUND_COLOR)
card_front_image = PhotoImage(file = r"images\card_front.png")
card_back_image = PhotoImage(file = r"images\card_back.png")
card_background = canvas.create_image(400, 263, image = card_front_image)
card_title = canvas.create_text(400, 150, text = "", font = ("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text = "", font = ("Ariel", 60, "bold"))
canvas.grid(column = 0, row = 0, columnspan = 2)

# Right / Wrong Buttons
cross_image = PhotoImage(file = r"images\wrong.png")
unknown_button = Button(image = cross_image, bg = BACKGROUND_COLOR, highlightthickness = 0, command = next_card) 
unknown_button.grid(column = 0, row = 1)
check_image = PhotoImage(file = r"images\right.png")
known_button = Button(image = check_image, bg = BACKGROUND_COLOR, highlightthickness = 0, command = is_known) 
known_button.grid(column = 1, row = 1)

next_card()

window.mainloop()