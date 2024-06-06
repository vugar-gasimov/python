from tkinter import *
from tkinter import messagebox
import pandas as pd

import random
# from random import choice, randint, shuffle
# import pyperclip
# import json
BG_COLOR = "#B1DDC6"
PATH_TO_ORIGINAL_DATA = r"day31\flash_card_app\data\100_poslih_top_words.csv"
PATH_TO_NEW_DATA = r"day31\flash_card_app\data\needed_words.csv"
current_card = {}
to_learn ={}

# ---------------------------- Data ------------------------------- #
try:
    data = pd.read_csv(PATH_TO_NEW_DATA)
except FileNotFoundError:
    # day31\flash_card_app\100_poslih_top_words.csv
    original_data = pd.read_csv(PATH_TO_ORIGINAL_DATA)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------------------------- U Input Handling ------------------------------- #

def next_card():
    
    global current_card, switch_timer
   
    window.after_cancel(switch_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Polish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Polish"], fill="black")
    canvas.itemconfig(canvas_img, image=canvas_img_front)
    switch_timer = window.after(3000, func=switch_card)
    # word = polish_words.sample(random_index).squeeze()

# ---------------------------- Switching Card ------------------------------- #

def switch_card():
    
    canvas.itemconfig(canvas_img, image=canvas_img_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    window.after_cancel(switch_card)
    

# ---------------------------- Right Btn Hangle ------------------------------- #
def right_clicked():
    
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv(PATH_TO_NEW_DATA, index=False)
    next_card()
    
# ---------------------------- Wrong Btn Hangle ------------------------------- #
def wrong_clicked():
  
    next_card()
    




    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BG_COLOR)
canvas = Canvas( height=530, width=800, bg=BG_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

switch_timer = window.after(3000, func=switch_card)

canvas_img_back = PhotoImage(file=r"day31\flash_card_app\images\card_back.png")
canvas_img_front = PhotoImage(file=r"day31\flash_card_app\images\card_front.png")

wrong_img = PhotoImage(file=r"day31\flash_card_app\images\wrong.png")
right_img = PhotoImage(file=r"day31\flash_card_app\images\right.png")
canvas_img = canvas.create_image(400, 265, image=canvas_img_front )
card_title = canvas.create_text(400, 150, text="polish", fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", fill="black", font=("Arial", 40, "bold"))
# language_label = Label(text="Language ",  height=2,)
# language_label.grid(row=1, column=0, )

# word_label = Label(text="Website: ",  height=2 )
# word_label.grid(, column=0, )


wrong_btn = Button(window, image=wrong_img,  bg=BG_COLOR, highlightthickness=0,  command=wrong_clicked)
wrong_btn.grid(row=1, column=0)


right_btn = Button(window, image=right_img, bg=BG_COLOR, highlightthickness=0, command=right_clicked)
right_btn.grid(row=1, column=1 )

next_card()




window.mainloop()