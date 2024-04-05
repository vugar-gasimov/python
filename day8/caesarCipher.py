import caesarCipherArt
print(caesarCipherArt.logo)
print("\n Welcome to caesar cipher which is a way of coding messages which have been used by Caesar \n")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caeser(plain_text, shift_amount, direction):
        cipher_text=""
        for char in plain_text:
            if char in alphabet:
                if direction == "encode":
                    shifted_index = (alphabet.index(char) + shift_amount) % len(alphabet)               
                elif direction == "decode":
                    shifted_index = (alphabet.index(char) - shift_amount) % len(alphabet)                    
                cipher_text += alphabet[shifted_index]
            else:
                cipher_text += char
        if direction == "encode" or direction == "decode":
            print(f"The {direction}d text is {cipher_text}")
        else:
            print("You didn't choose 'encode' or 'decode' (Try again).")
    caeser(plain_text=text, shift_amount=shift, direction=direction)
    while True:
        if_continue = input("\n Would you like to encode or decode more ? (yes/no): ").lower()
        if if_continue == "yes":
            break
        elif if_continue == "no":
            print(" \n Thanks for using our coding program and goodbye.")
            exit()
        else:
            print(" \n Invalid input. Please enter 'yes' or 'no'.")

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#       shift_amount *= -1
#   for letter in start_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     end_text += alphabet[new_position]
#   print(f"Here's the {direction}d result: {end_text}")

# def encrypt(plain_text, shift_amount):
#     cipher_text=""
#     for char in plain_text:
#         if char in alphabet:
#             shifted_index = (alphabet.index(char)+ shift_amount) % len(alphabet)
#             cipher_text += alphabet[shifted_index]
#         else:
#             cipher_text += char
             
#     print(f"The encoded text is {cipher_text}")
    
# def decrypt(plain_text, shift_amount):
#     cipher_text=""
#     for char in plain_text:
#         if char in alphabet:
#             shifted_index = (alphabet.index(char) - shift_amount) % len(alphabet)
#             cipher_text += alphabet[shifted_index]
#         else:
#             cipher_text += char
             
#     print(f"The decoded text is {plain_text}")
        
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(plain_text=text, shift_amount=shift)
    
