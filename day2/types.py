num_char = len(input("What is your name? "))

print(type(num_char))

new_num_char= str(num_char)

print("Your name is " + new_num_char + " characters long.") 

char_digit = input()
first_digit = int(char_digit[0])
second_digit = int(char_digit[1])
print(first_digit+second_digit)

height = input()
weight = input()

weight_as_int = int(weight)
height_as_float = float(height)
# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi_as_int)