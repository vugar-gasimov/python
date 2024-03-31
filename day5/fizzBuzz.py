print("\n Welcome to FizzBuzz game \n")
print(" Fizz Buzz is a simple game that helps children learn about numbers and multiples. \n - Here's a simple explanation: \n - Children sit in a circle or stand in a line. \n - Starting from the number 1, each child says the next number in sequence. \n - When a number is a multiple of 3, instead of saying the number, the child says 'Fizz'. \n - When a number is a multiple of 5, instead of saying the number, the child says 'Buzz'. \n - If a number is both a multiple of 3 and 5, the child says 'FizzBuzz' instead of the number. \n - The game continues until all the children have had a turn, reaching a predetermined maximum number.")

fizz_buzz = int(input("\n Enter max fizz buzz number "))
# fizz_buzz = 100

all_number = 0

for number in range(1, fizz_buzz + 1):
  if number % 3 == 0 and number % 5 == 0:
    all_number += 1
    print("FizzBuzz")
  elif number % 3 == 0:
    all_number += 1
    print("Fizz")
  elif number % 5 == 0:
    all_number += 1
    print("Buzz")
  else:
    all_number += 1
    print(all_number)