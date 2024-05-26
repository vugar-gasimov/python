from tkinter import *

def convert_btn():
    
    mile = float(input.get())
    km = mile * 1.60934
    output["text"] = f"{km}" 
    
    

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

input = Entry(width=20, )
input.insert(END, string="0")
input.focus()
input.grid(column=1, row=0)

miles_label = Label(text="Miles", padx=20, pady=20, font=("Arial", 18, ))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", padx=20, pady=20, font=("Arial", 18, ))
equal_label.grid(column=0, row=1)

output = Label(text="0", padx=20, pady=20, font=("Arial", 18, ))
output.grid(column=1, row=1)

km_label = Label(text="Km", padx=20, pady=20, font=("Arial", 18, ))
km_label.grid(column=2, row=1)

button=Button(text="Calculate", command=convert_btn)
button.grid(column=1, row=2)



window.mainloop()