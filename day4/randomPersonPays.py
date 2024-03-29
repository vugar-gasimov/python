import random
names_string = input("Enter names which can pay for the meal. ")
names = names_string.split(", ")


names_list = len(names)
random_index = random.randint(0, names_list -1)
random_name = names[random_index]
print(random_name + " is going to buy the meal today!")