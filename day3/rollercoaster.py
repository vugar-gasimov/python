print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm ? :"))
bill = 0
if height >= 120:
  print("You are tall enough to ride the rollercoaster ")
  age = int(input("What is your age? "))
  if age < 12:
    # print("Please pay $5 for ticket")
    bill = 5
  elif age <= 18:
    # print("Please pay $7 for ticket")
     bill = 7
  elif age >= 45 and age <= 55:
     print("Everything is gonna be ok. Have a free ride on us!")
     bill = 0
  else:
    #print("Please pay $12 for ticket")
    bill = 12
  wants_photo = input("Do you want your photo to be taken while riding? y or n ")
  if wants_photo == "Y":
      bill = bill + 3
      # this is shorter  bill += 3
      you_payed = int(input(f"Your bill is ${bill} please pay for ticket"))
      if you_payed >= 8:
          print("Here is your ticket and please wait in line")
      else:
          print("If you can't pay, sorry we can't give you free ticket.")
  else:
      you_payed = int(input(f"Your bill is ${bill} please pay and wait in the line"))
else:
    print("Sorry, you have to grow taller before you can ride. ")