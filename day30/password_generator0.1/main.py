from tkinter import *
from tkinter import messagebox
from random import choice, randint,shuffle
import pyperclip
import json
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    # password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_letters = [choice(letters) for _ in range( randint(8, 10))]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_symbols =[choice(symbols) for _ in range(randint(2, 4))]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    
    password_numbers =[choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters+password_symbols+password_numbers

    shuffle(password_list)
    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    password_entry.insert(0, password)
    # print(f"Your password is: {password}")
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    website = website_entry.get()
    email = email_uname_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    
    
    
    if len(website) == 0 or len(email) == 0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
     
        
        try:
            with open(r"day30\password_generator0.1\data.json", mode="r") as f:
                
                # f.write(f"{website} | {email} | {password} \n")  
                # Reading old data
                data = json.load(f)
                # Updating old data with new data
                # data.update(new_data)
            # with open(r"day30\password_generator0.1\data.json", mode="w") as f:
            #     json.dump(data, f, indent=4)   
            #     website_entry.delete(0, END)
            #     password_entry.delete(0, END)
        except FileNotFoundError:   
            with open(r"day30\password_generator0.1\data.json", mode="w") as f:
                # Saving updated data
                json.dump(new_data, f, indent=4)  
        else: 
            # Updating old data with new data
            data.update(new_data)
            
            with open(r"day30\password_generator0.1\data.json", mode="w") as f:
                json.dump(data, f, indent=4)   
        finally:    
            website_entry.delete(0, END)
            password_entry.delete(0, END)
                # print(data)
   
            
    

# ---------------------------- Search Existing Password ------------------------------- #

def search_website():
    website = website_entry.get()
    try:
        with open("day30\password_generator0.1\data.json") as f:
            data = json.load(f)  
            
    except FileNotFoundError: 
        messagebox.showinfo(title="Not Found", message="You haven't added any passwords, before search add passwords.")  
        
    else:
        if website in data:
            # email = data[website]
            # 'email': 'vugar@gmail.com', 'password': 'na9XbiUM3Nf)3$9g'
            email = data[website]["email"]
            # 'email': 'vugar@gmail.com', 
            password = data[website]["password"]
            messagebox.showinfo(title=f"Your {website} password is found.", message=f"Your email is {email} \n Your password is {password}")
        else:
            messagebox.showinfo(title="Not Found Error", message=f"In name {website} nothing found")
            

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50,  bg=GREEN)

canvas = Canvas(width=200, height=200, bg=GREEN, highlightthickness=0)
logo_img = PhotoImage(file=r"day29\password_generator\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", bg=GREEN, height=2 )
website_label.grid(row=1, column=0, )

website_entry = Entry(width=21, bg=RED )
website_entry.grid(row=1, column=1,   )
website_entry.focus()

search_btn = Button(text="Search", bg=PINK, command=search_website, width=14 )
search_btn.grid(row=1, column=2, )

email_uname_label = Label(text="Email/Username: ", bg=GREEN, height=2 )
email_uname_label.grid(row=2, column=0, )
email_uname_entry = Entry(width=39, bg=RED )
email_uname_entry.grid(row=2, column=1, columnspan=2)
email_uname_entry.insert(0, "vugar@gmail.com")

password_label = Label(text="Password: ", bg=GREEN, height=2 )
password_label.grid(row=3, column=0, )

password_entry = Entry(width=21, bg=RED )
password_entry.grid(row=3, column=1, )

generate_password_btn = Button(text="Generate Password", bg=PINK, command=generate_password, width=14 )
generate_password_btn.grid(row=3, column=2, )

add_btn = Button(text="Add", width=36, bg=PINK, command=save, )
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()