# file_path = "../../../Desktop/my_file.txt"
"../../../../Documents/GitHub/python/day24/main.py"
"../../../../Desktop/my_file.txt"
"../../../Desktop/my_file.txt"
# C:\Users\vuqar\OneDrive\Documents\GitHub\python\day24
# file_path = r"\Users\vuqar\OneDrive\Desktop/my_file.txt"
# file_path = "C:/Users/vuqar/OneDrive/Desktop/my_file.txt"
# file_path = "day24\my_file.txt"
# new_file_path = "day24\my_new_file.txt"
# with open(file_path, mode="r") as file:
# # # file = open(file_path)
#     print(file)
#     file_content = file.read()
#     print(file_content)
# # file.close()

# with open(file_path, mode="a") as file:
#     file.write("\n New text.")
# with open(new_file_path, mode="w") as file:
#     file.write("\n New text.")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    
# with open(r"day24\Input\letters\starting_letter.txt", mode="r") as example:
#     letter = example.read()
#     print(letter)
    
# with open(r"day24\Input\names\invited_names.txt", mode="r") as file_names:
#     # day24\Input\names
#     copy_of_names = file_names.read()
#     print(copy_of_names)
    
# names = copy_of_names.splitlines()

# for name in names:
#     new_letter = letter.replace("[name]", name)
#     with open(fr"day24\Output\ReadyToSend\letter_for_{name}.txt", mode="w") as output_letter:
#     # day24\Input\names
#         output_letter.write(new_letter)
#     print(new_letter)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

with open(r"day24\Input\letters\starting_letter.txt", mode="r") as example:
    letter = example.read()
    print(letter)
    
with open(r"day24\Input\names\invited_names.txt", mode="r") as file_names:
    names = file_names.readlines()
    
# names = [name.strip()for name in names]
for name in names:
    name = name.strip()
    new_letter = letter.replace("[name]", name)
    with open(fr"day24\Output\ReadyToSend\letter_for_{name}.txt", mode="w") as output_letter:

        output_letter.write(new_letter)
    print(new_letter)
