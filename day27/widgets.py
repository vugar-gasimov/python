# import tkinter
from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program Wisth Python")
window.minsize(width=500, height=500)

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.place(x=0, y=0)
# my_label.pack()

    
button=Button(text="Click Me", command=button_clicked)
button.pack()


# Entry

input = Entry(width=80)
input.insert(END, string="Some text to begin with.")
input.pack()
# input.get()

# Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

# Spinbox
def spinbox_used():
    print(spinbox.get())
    
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
# Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=10, command=scale_used)
scale.pack()

# CheckButton
def checkbutton_used():
    # Prints 1 if checked otherwise 0.
    print(checked_state.get())
checked_state = IntVar()
checkbutton = Checkbutton(text = "Is it On?", variable = checked_state, command = checkbutton_used)

checked_state.get()
checkbutton.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))
#Listbox with three values. When an item is clicked, prints it's index to console.
listbox = Listbox(height=4)
fruits= ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind('<<ListboxSelect>>', listbox_used)
listbox.pack()






window.mainloop()