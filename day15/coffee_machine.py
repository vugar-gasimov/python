from resources import resources
from art import coffee_machine_img

def coffee_machine():
    print("Hello, Welcome to our coffee machine. ☕")
    work = True
    order = input("What would you like? (espresso/latte/cappuccino): ") 
    while work:
        if order == "off":
            work = False
            
        if order == "report":
            print(resources)
            coffee_machine()
            
        if order == "water":
            resources["water"] += 250
            print(resources)
            coffee_machine()
            
        if order == "milk":
            resources["milk"] += 250
            print(resources)
            coffee_machine()
            
        if order == "coffee":
            resources["coffee"] += 100
            print(resources)
            coffee_machine()
            
        if order == "espresso":
            if resources["water"] < 50:
                print("Sorry there is not enough water. 🫗")
                coffee_machine()
            elif resources["coffee"] < 18:
                print("Sorry there is not enough coffee. 🫘")
                coffee_machine()
            else:
                print("You should pay 1.5$")
                quarters = float(input("How many quarters: "))
                dimes = float(input("How many dimes: "))
                nickles = float(input("How many nickles: "))
                pennies = float(input("How many pennies: "))
                total_pay = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
                if total_pay < 1.5:
                    print("Sorry that's not enough money. Money refunded.")
                    coffee_machine()
                elif total_pay > 1.5:
                    change = total_pay - 1.5
                    print(f"Here is ${change} dollars in change.")
                    print("Here is your espresso. Enjoy!")
                    resources["coffee"] -= 18
                    resources["water"] -= 50
                    resources["Money"] += 1.5
                    coffee_machine()
                elif total_pay == 1.5:
                    print("Here is your espresso. Enjoy!")
                    resources["coffee"] -= 18
                    resources["water"] -= 50
                    resources["Money"] += 1.5
                    coffee_machine()
                    
        if order == "latte":
            if resources["water"] < 200:
                print("Sorry there is not enough water. 🫗")
                coffee_machine()
            elif resources["coffee"] < 24:
                print("Sorry there is not enough coffee. 🫘")
                coffee_machine()
            elif resources["milk"] < 150:
                print("Sorry there is not enough milk. 🥛 ")
                coffee_machine()
            else:
                print("You should pay 2.5$")
                quarters = float(input("How many quarters: "))
                dimes = float(input("How many dimes: "))
                nickles = float(input("How many nickles: "))
                pennies = float(input("How many pennies: "))
                total_pay = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
                if total_pay < 2.5:
                    print("Sorry that's not enough money. Money refunded.")
                    coffee_machine()
                elif total_pay > 2.5:
                    change = total_pay - 2.5
                    print(f"Here is ${change} dollars in change.")
                    print("Here is your latte. Enjoy!")
                    resources["milk"] -= 150
                    resources["coffee"] -= 24
                    resources["water"] -= 200
                    resources["Money"] += 2.5
                    coffee_machine()
                elif total_pay == 2.5:
                    print("Here is your latte. Enjoy!")
                    resources["milk"] -= 150
                    resources["coffee"] -= 24
                    resources["water"] -= 200
                    resources["Money"] += 2.5
                    coffee_machine()
        if order == "cappuccino":
            if resources["water"] < 250:
                print("Sorry there is not enough water. 🫗")
                coffee_machine()
            elif resources["coffee"] < 24:
                print("Sorry there is not enough coffee. 🫘")
                coffee_machine()
            elif resources["milk"] < 100:
                print("Sorry there is not enough milk. 🥛")
                coffee_machine()
            else:
                print("You should pay 3.0$")
                quarters = float(input("How many quarters: "))
                dimes = float(input("How many dimes: "))
                nickles = float(input("How many nickles: "))
                pennies = float(input("How many pennies: "))
                total_pay = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
                if total_pay < 3.0:
                    print("Sorry that's not enough money. Money refunded.")
                    coffee_machine()
                elif total_pay > 3.0:
                    change = total_pay - 3.0
                    print(f"Here is ${change} dollars in change.")
                    print("Here is your cappuccino. Enjoy!")
                    resources["milk"] -= 100
                    resources["coffee"] -= 24
                    resources["water"] -= 250
                    resources["Money"] += 3.0
                    coffee_machine()
                elif total_pay == 3.0:
                    print("Here is your cappuccino. Enjoy!")
                    resources["milk"] -= 100
                    resources["coffee"] -= 24
                    resources["water"] -= 250
                    resources["Money"] += 3.0
                    coffee_machine()
print(coffee_machine_img)
condition = input("Coffee Machine (on/off): ")
while condition == "off":
    if condition == "off":
        condition = input("Coffee Machine (on/off): ")

if condition == "on":
    coffee_machine()