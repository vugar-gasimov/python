from resources import resources

def coffee_machine():
    print("Hello, Welcome to our coffee machine. ☕")
    work = True
    order = input("What would you like? (espresso/latte/cappuccino): ") 
    while work:
        if order == "off":
            work = False
            
        if order == "report":
            print(resources)
            
        if order == "espresso":
            if resources["water"] < 50:
                print("Sorry there is not enough water.")
            elif resources["coffee"] < 18:
                print("Sorry there is not enough coffee.")
            else:
                print("You should pay 1.5$")
                quarters = float(input("How many quarters"))
                dimes = float(input("How many dimes"))
                nickles = float(input("How many nickles"))
                pennies = float(input("How many pennies"))
                total_pay = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.5) + (pennies * 0.01)
                if total_pay < 1.5:
                    print("Sorry that's not enough money. Money refunded.")
                elif total_pay > 1.5:
                    change = total_pay - 1.5
                    print(f"Here is ${change} dollars in change.")
                    print("Here is your espresso. Enjoy!")
                    resources["Money"] += 1.5
                    coffee_machine()
                elif total_pay == 1.5:
                    print("Here is your espresso. Enjoy!")
                    resources["Money"] += 1.5
                    coffee_machine()
                
condition = input("Coffee Machine on/off: ")
if condition == "off":
    while condition == "on":
        condition = input("Coffee Machine on/off: ")
else:
    coffee_machine()