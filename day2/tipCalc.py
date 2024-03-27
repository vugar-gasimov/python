"Welcome to the tip calculator "
"What was the total bill? "
"How much tip would you like to give? "
"How many people to split the bill? "

# Will use rounded with two decimal
# Give three examples in percentage.

# print(" Welcome to the tip calculator! ")
# total_bill = input("What was the total bill? $")

# preferred_tip =  input("How much tip would you like to give? 10, 12, or 15 ? ")
# tip_for_bill = int(preferred_tip) / 100 * float(total_bill)
# amount_people_pay = input("How many people to split the bill? ")
# total_bill_with_tip = float(total_bill) + round(tip_for_bill,2)
# each_persons_bill = total_bill_with_tip / int(amount_people_pay)
# print(f"Each person should pay: ${round(each_persons_bill, 2)} ")

print(" Welcome to the tip calculator! ")
total_bill = float(input("What was the total bill? $"))

preferred_tip =  int(input("How much tip would you like to give? 10, 12, or 15 ? %"))
tip_for_bill = preferred_tip / 100 * total_bill
amount_people_pay = int(input("How many people to split the bill? "))
total_bill_with_tip = total_bill + round(tip_for_bill,2)
each_persons_bill = total_bill_with_tip / amount_people_pay
each_bill_final=round(each_persons_bill, 2)
each_bill_final="{:.2f}".format(each_persons_bill)
print(f"Each person should pay: ${ each_bill_final}")