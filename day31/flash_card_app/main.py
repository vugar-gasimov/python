from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
# from random import choice, randint, shuffle
# import pyperclip
# import json
BG_COLOR = "#B1DDC6"

# ---------------------------- U Input Handling ------------------------------- #

def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Polish")
    canvas.itemconfig(card_word, text=current_card["Polish"])
  
    # word = polish_words.sample(random_index).squeeze()


# ---------------------------- Data ------------------------------- #

try:
    # with open(r"day31\flash_card_app\100_poslih_top_words.csv", mode="r") as f:            
    #     data = f.readlines(r"day31\flash_card_app\100_poslih_top_words.csv",)
    data = pd.read_csv(r"day31\flash_card_app\100_poslih_top_words.csv")
    
except FileNotFoundError:   
    messagebox.showinfo(title="File Not Found", message="Oops, something went wrong seems like we can fine the file containing the words.!")
else: 
    to_learn = data.to_dict(orient="records")

    # language = data.Polish.to_list()
    # polish_words = data['Polish']
    # word = polish_words.sample().squeeze()
    # polish = data.columns[0]
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BG_COLOR)
canvas = Canvas( height=530, width=800, bg=BG_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

canvas_img_back = PhotoImage(file=r"day31\flash_card_app\images\card_back.png")
canvas_img_front = PhotoImage(file=r"day31\flash_card_app\images\card_front.png")

wrong_img = PhotoImage(file=r"day31\flash_card_app\images\wrong.png")
right_img = PhotoImage(file=r"day31\flash_card_app\images\right.png")
canvas.create_image(400, 265, image=canvas_img_front )
card_title = canvas.create_text(400, 150, text="polish", fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", fill="black", font=("Arial", 40, "bold"))
# language_label = Label(text="Language ",  height=2,)
# language_label.grid(row=1, column=0, )

# word_label = Label(text="Website: ",  height=2 )
# word_label.grid(, column=0, )


wrong_btn = Button(window, image=wrong_img,  bg=BG_COLOR, highlightthickness=0,  command=next_card)
wrong_btn.grid(row=1, column=0)


right_btn = Button(window, image=right_img, bg=BG_COLOR, highlightthickness=0, command=next_card)
right_btn.grid(row=1, column=1 )

next_card()



window.mainloop()