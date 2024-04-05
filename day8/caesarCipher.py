alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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
    
