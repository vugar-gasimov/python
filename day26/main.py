# numbers = [1, 2, 3]
# new_list = []
# # for n in numbers: 
# #     add_1 = n + 1
# #     new_list.append(add_1)
# # print(new_list)
# # Or
# new_list = [n + 1 for n in numbers]

# print(new_list)
# name = "Vugar"
# new_list = [l for l in name]
# print(new_list)
# range(1,5)
# range_list = [n * 2 for n in range(1,5 +1)]
# print(range_list)
# names = [ "Alice",  "Bob",   "Charlie",   "Diana",   "Eve",   "Frank",   "Grace",   "Hank",   "Ivy",    "Jack",    "Karen",  "Leo", "Mona", "Nina",  "Oscar",   "Paul",    "Quinn",   "Rita",    "Sam",    "Tina",    "Uma",    "Vince",    "Wendy", "Xander","Yara", "Zane"
# ]
# short_names = [ n for n in names if len(n) < 5 ]
# long_names = [ n for n in names if len(n) > 4 ]
# l_n_uppercase = [n.upper() for n in names if len(n) > 4]
# print(f"Short names:  {short_names}")
# print(f"Long names:  {long_names}")
# print(f"Long names upper case:  {l_n_uppercase}")

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# squared_numbers = [ n * n for n in numbers]

# print(squared_numbers)

# list_of_strings = input().split(',')

# list_of_numbers = [int(n) for n in list_of_strings]

# result = [n for n in list_of_numbers if n % 2 == 0]


# print(result)

# with open("file1.txt") as data1:
#   list1 = data1.readlines()
# with open("file2.txt") as data2:
#   list2 = data2.readlines() 

# result = [ int(n) for n in list1 if n in list2]

# print(result)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# names = [ "Alice",  "Bob",   "Charlie",   "Diana",   "Eve",   "Frank",   "Grace",   "Hank",   "Ivy",    "Jack",    "Karen",  "Leo", "Mona", "Nina",  "Oscar",   "Paul", "Vugar",   "Quinn",   "Rita",    "Sam",    "Tina",    "Uma",    "Vince",    "Wendy", "Xander", "Yara", "Zane"
# ]

# # student_score = {
# #     "Alex": 80,
# #     "Beth": 78,
# # }
# import random
# # student_score = {new_key:new_value for item in list}
# student_score = {student:random.randint(30, 100) for student in names}

# # passed_students = {
# #     "Alex": 80,
# #     "Beth": 78,
# # }

# passed_students = {student:score for (student,score) in student_score.items() if score >= 60 }
# not_passed_students = {student:score for (student,score) in student_score.items() if score < 60 }

# print(f"\nAll students with scores: {student_score}\n")
# print(f"All passed students with scores: {passed_students}\n")
# print(f"All not passed students with scores: {not_passed_students}\n")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# sentence = input()

# result = {word:len(word) for word in sentence.split()}

# print(result)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# eval() converts correctly formatted string to dict
# weather_c = eval(input())

# # dictionary comprehension
# weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}

# print(weather_f)












