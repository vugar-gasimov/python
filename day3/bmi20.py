
height = float(input("Enter your height in meters e.g., 1.55: "))

weight = int(input("Enter your weight in kilograms e.g., 72: "))

bmi = weight / (height * height)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >= 18.5:
  if bmi < 25:
   print(f"Your BMI is {bmi}, you have a normal weight.")
  elif bmi >= 25:
   if bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
   elif bmi >= 30: 
    if bmi < 35:
     print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")