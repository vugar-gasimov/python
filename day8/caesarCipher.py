alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            shifted_index = (alphabet.index(char)+ shift_amount) % len(alphabet)
            cipher_text += alphabet[shifted_index]
        else:
            cipher_text += char
             
    print(f"The encoded text is {cipher_text}")
    
def decrypt(plain_text, shift_amount):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            shifted_index = (alphabet.index(char) - shift_amount) % len(alphabet)
            cipher_text += alphabet[shifted_index]
        else:
            cipher_text += char
             
    print(f"The encoded text is {cipher_text}")
        
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(plain_text=text, shift_amount=shift)
    
