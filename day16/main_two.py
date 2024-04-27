from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while is_on:
    options = menu.get_items()
    drink_choice = input(f"What would you like to order? ({options}): ")
    if drink_choice == "off":
        print("You turned off the coffee machine.")
        is_on = False
    elif drink_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        found_drink = menu.find_drink(drink_choice)  
        if coffee_maker.is_resource_sufficient(found_drink):
            print(f"You have ordered a {found_drink.name}. The price is ${found_drink.cost}.")
            if money_machine.make_payment(found_drink.cost):
                coffee_maker.make_coffee(found_drink)
        else:
            print(f"Sorry, the '{drink_choice}' is not available.")
            
    
    
