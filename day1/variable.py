myName = input("What is my name? ")
print("My name is " + myName)
print("Your name's lenght is ", len(input("If you want to know your name's length write your name ")))

# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇
first = a
second = b
a = second
b =first

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)