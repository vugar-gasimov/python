# def greet():
#     name = input("Hello, What is your name? ")
#     print(f"Greetings dear {name}")
#     age = input(f"Dear {name}, how old are you? ")
#     hobbies = input(f"Dear {name}, what are your hobbies? ").split(", ")
    
# greet()

# def greet_name(name):
#     print(f"Greetings dear {name}")
#     print(f"Dear {name}, What is your surname? ")
#     print(f"Dear {name}, how old are you? ")
#     print(f"Dear {name}, what are your hobbies? ")
    
# greet_name("Vugar")

# def greet_name(name, location):
#     print(f"Greetings dear {name}")
#     print(f"Dear {name}, What is your surname? ")
#     print(f"Dear {name}, How is the weather in {location}? ")
#     print(f"Dear {name}, how old are you? ")
#     print(f"Dear {name}, what are your hobbies? ")
    
# greet_name("Vugar", "Kyiv")
def greet_name_with_loc(name="Vugar", location="Kyiv"):
    print(f"Greetings dear {name}")
    print(f"Dear {name}, What is your surname? ")
    print(f"Dear {name}, How is the weather in {location}? ")
    print(f"Dear {name}, how old are you? ")
    print(f"Dear {name}, what are your hobbies? ")
    
greet_name_with_loc("Gasimov", "Lusondorf")