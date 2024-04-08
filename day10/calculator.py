import art
print("\n Welcome to Calculator program ")

def add(n1, n2):
    """Adds two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts two numbers."""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies two numbers."""
    return(n1 * n2)

def divide(n1, n2):
    """Divides two numbers."""
    return(n1 / n2)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    
}
def calculator():
    """Allows the user to perform multiple arithmetic operations."""
    print(art.logo)
    
    num1 = float(input("What is the first number: "))

    continue_answer = True
    while continue_answer:
        for operation in operations:
            print(f"Choose an {operation}")
        
        active_operation = input("Pick an operation: ")[0]

        num2 = float(input("What is the next number: "))

# My way
# def collector(num1, num2, active_operation):
#     if active_operation == "+":
#         return add(num1, num2)
#     elif active_operation == "-":
#         return subtract(num1, num2)
#     elif  active_operation == "*":
#         return multiply(num1, num2)
#     elif active_operation == "/":
#         return divide(num1, num2)
#     else:
#         return "You picked a not existing operation. Please pick again."
        
# calc_answer = collector(num1=num1, num2=num2, active_operation=active_operation)
# Teacher's way
        collector = operations[active_operation]
        answer = collector(num1, num2)
            
        print(f"{num1} {active_operation} {num2} = {answer}")   
        to_continue_answer = input(f"\n Type 'y' to continue calculating with {answer}, or Type 'n' to start a new calculation. ")[0].lower()
        if to_continue_answer == "y":
            continue_answer = True
            num1 = answer
        else:
            continue_answer = False
            calculator()
calculator()       
    # active_operation = input("Pick another operation: ")

    # num3 = int(input("What is the next number: "))

    # collector = operations[active_operation]
    # second_answer = collector(answer, num3)
    # print(f"{answer} {active_operation} {num3} = {second_answer}")
    
    # to_continue_answer = input(f"\n Type 'y' to continue calculating with {second_answer}, or Type 'n' to exit. ")[0].lower()

