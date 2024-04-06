programming_dictionary = {
    "Bug": "\n An error in a program that prevents the program from running as expected. \n", 
    "Function": "\n A piece of code that you can easily call over and over again. \n",
    "Loop": "\n The action of doing something over and over again. \n"
    }

# print(programming_dictionary["Bug"])

# programming_dictionary["While_Loop"] = "\n A while loop is a control flow statement in programming that allows you to repeatedly execute a block of code as long as a specified condition is true. It keeps iterating until the condition becomes false. \n"

# print(programming_dictionary)

# empty_dictionary = {}
# programming_dictionary = {}

# programming_dictionary["Function"] = "\n A piece of code that you can easily call over and over again. And it can have inside other functions and loos etc.  \n"

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])