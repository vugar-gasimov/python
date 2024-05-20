file_path = "../../../Desktop/my_file.txt"
"../../../../Documents/GitHub/python/day24/main.py"
"../../../../Desktop/my_file.txt"
"../../../Desktop/my_file.txt"
# C:\Users\vuqar\OneDrive\Documents\GitHub\python\day24
# file_path = r"\Users\vuqar\OneDrive\Desktop/my_file.txt"
# file_path = "C:/Users/vuqar/OneDrive/Desktop/my_file.txt"
# file_path = "day24\my_file.txt"
# new_file_path = "day24\my_new_file.txt"
with open(file_path, mode="r") as file:
# # file = open(file_path)
    print(file)
    file_content = file.read()
    print(file_content)
# # file.close()

# with open(file_path, mode="a") as file:
#     file.write("\n New text.")
# with open(new_file_path, mode="w") as file:
#     file.write("\n New text.")