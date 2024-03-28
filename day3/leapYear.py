#
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:  # Check for century years
    if year % 400 == 0:  # Exception for divisible by 400
      print(f"{year} is a leap year.")
    else:
      print(f"{year} is not a leap year.")
  else:
    print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")