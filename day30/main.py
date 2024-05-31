# FileNotFound

# try:
#     file = open("file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["fsfs"])
# except FileNotFoundError:
#     file = open(r"day30\file.txt", "w")
#     file.write("Something")
#     # print("There was an error.")
# except KeyError as e:
#     print(f"The key {e} does not exist.")
#     print(f"KeyError: {e}")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")
    # file.close()
    # print("File was closed.")
    
    
# height = float(input("Height: "))
# weight = int(input("Weight: "))
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")
# # bmi = weight / (height * height)
# bmi = weight / height ** 2
# print(bmi)


# fruits = eval(input())

# def make_pie(index):
#     try:
#       fruit = fruits[index]

#     except IndexError:
#       print("Fruit pie")
#     else:
#       print(fruit + " pie")
      
# make_pie(4)

# facebook_posts = eval(input())

# total_likes = 0
# # Catching the KeyError exception in the dictionary
# for post in facebook_posts:
#   try:
#     total_likes = total_likes + post['Likes']
#   except KeyError:
#     pass 

# print(total_likes)