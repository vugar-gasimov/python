# name = input("Enter your name: ")
# surname =input("Enter your surname: ")

def format_name(f_name, s_name):
    """ Therefore, month_days[month - 1] calculates the correct index in the month_days list based on the input month and retrieves the corresponding number of days for that month. """
    if f_name == "" or s_name == "":
        return "You didn't enter valid inputs."
    first_name = f_name.title()
    second_name = s_name.title()
    # return first_name, second_name
    return f"Result: {first_name}, {second_name}"

# print(format_name(f_name=name, s_name=surname))
print(format_name(input("Enter your name: "),input("Enter your surname: ")))
format_name()