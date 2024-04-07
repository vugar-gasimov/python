name = input("Enter your name: ")
surname =input("Enter your surname: ")

def format_name(f_name, s_name):
    first_name = f_name.title()
    second_name = s_name.title()
    return first_name, second_name

print(format_name(f_name=name, s_name=surname))
