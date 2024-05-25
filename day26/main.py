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
names = [ "Alice",  "Bob",   "Charlie",   "Diana",   "Eve",   "Frank",   "Grace",   "Hank",   "Ivy",    "Jack",    "Karen",  "Leo", "Mona", "Nina",  "Oscar",   "Paul",    "Quinn",   "Rita",    "Sam",    "Tina",    "Uma",    "Vince",    "Wendy", "Xander","Yara", "Zane"
]
short_names = [ n for n in names if len(n) < 5 ]
long_names = [ n for n in names if len(n) > 4 ]
l_n_uppercase = [n.upper() for n in names if len(n) > 4]
print(f"Short names:  {short_names}")
print(f"Long names:  {long_names}")
print(f"Long names upper case:  {l_n_uppercase}")
