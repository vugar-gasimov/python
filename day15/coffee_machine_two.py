from resources import resources
# from art import coffee_machine_img
from menu import MENU


profit = 0


def is_resources_sufficient(order_ingredients):
    """Returns True when the order can be made, and False if there are insufficient ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
    
    
def process_coins():
    """Returns the total amount calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}, ☕ Enjoy.")
    
work = True

while work:
    order = input("What would you like? (espresso/latte/cappuccino): ") 
    
    if order == "off":
        print("Coffee machine turned off")
        work = False
    elif order == "report":
        print(f"   Water: {resources['water']}ml 🫗")
        print(f"   Milk: {resources['milk']}ml 🥛")
        print(f"   Coffee: {resources['coffee']}g 🫘")
        print(f"   Money: ${profit} 💵 ")
        # coffee_machine()
    else:
        drink = MENU[order]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])