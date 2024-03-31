import random

print("\n                            <<<Welcome to Py password generator!>>>")
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters= int(input("\n  How many letters would you like in your password? ")) 
nr_symbols = int(input(f"  How many symbols would you like? "))
nr_numbers = int(input(f"  How many numbers would you like? "))

password_one =""
for item in range(1, nr_letters + 1):
    password_one += random.choice(letters)
    
for item in range(1, nr_symbols + 1):
    password_one += random.choice(symbols)
    
for item in range(1, nr_numbers + 1):
    password_one += random.choice(numbers)
    
print(f"\n  - Password suggestion one: {password_one}")

randomised_pswd_second = ""

for item in range(len(password_one)):
    chosen_char = random.choice(password_one)
    randomised_pswd_second += chosen_char
    password_one = password_one.replace(chosen_char, '', 1)
        
print(f"  - Password suggestion two: {randomised_pswd_second} Recommended")


password_list = []
for item in range(1, nr_letters + 1):
    password_list += random.choice(letters)
    
for item in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
    
for item in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
    
random.shuffle(password_list)
password_third = ''
for item in password_list:
    password_third += item
    
print(f"  - Password suggestion three: {password_third}")