# import tkinter
from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program Wisth Python")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label["text"] = "New Text"
my_label.config(text="New Text", padx=20, pady=20)

my_label.grid(column=0, row=0)
# my_label.place(x=0, y=0)
# my_label.pack()

    
button=Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
# button.pack()

n_button=Button(text="Don't Click Me", command=button_clicked)
n_button.grid(column=2, row=0)


# Entry

input = Entry(width=80)
input.insert(END, string="Some text to begin with.")
input.grid(column=3, row=2)
# input.pack()
# input.get()







window.mainloop()