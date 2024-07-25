# one = {
#     "first_name": "Huseyin",
#     "last_name": "Agalarov",
#     "age": 24,
#     "city": "kiev",
#     "favorite_num": 7,
    
# }
# two={
#     "first_name": "Saleh",
#     "last_name": "Babakisiev",
#     "age": 34,
#     "city": "luisiana",
#     "nationality": "Azerbaijan",
#     "favorite_num": 6,
# }
# three = {
#     "first_name": "Huseyin",
#     "last_name": "Agalarov",
#     "age": 24,
#     "city": "kiev",
#     "favorite_num": 7,
    
# }
# four={
#     "first_name": "Saleh",
#     "last_name": "Babakisiev",
#     "age": 34,
#     "city": "luisiana",
#     "nationality": "Azerbaijan",
#     "favorite_num": 6,
# }
# friends = {
#    "one": one,
#    "two": two,
#    "three": three,
#    "four": four,
# }
# nationality_value_one = friends["one"].get("nationality", "No point value assigned.")
# nationality_value_two = friends["two"].get("nationality", "No point value assigned.")

# # print(friends["one"]["first_name"])
# # print(friends["one"]["age"])
# # print(nationality_value_one)
# # print(friends["two"]["first_name"])
# # print(friends["two"]["city"])
# # print(nationality_value_two)

# # print(friends["one"]["favorite_num"])
# # print(friends["two"]["favorite_num"])
# # print(friends["three"]["favorite_num"])
# # print(friends["four"]["favorite_num"])
# glossary = {
#     "key": "Key is like a name to access a value",
#     "traceback": "What happened before its trace",
#     "module": "Every line which can cause error",
#     "get": "To get something built in func",
#     "call": "To call each line and continue based on written code",
# }
# for word in glossary:
#     print(f"This word {word} means {glossary[word]} ")

# listOfNumbers = [1, 2, 3, 4, 5, 6]

# for number in listOfNumbers:
#     # print(number)
#     if (number % 2 == 0):
#         print(f"{number} is even")
#     else:
#         print(f"{number} is odd")
        
# print ("All done.")

# import numpy as np

# A = np.random.normal(25.0, 5.0, 10)
# print (A)
x = [1, 2, 3, 4, 5, 6]
# print(x[:3])
# print(x[3:])
# print(x[-2:])
x.extend([7,8])
# print(x)
x.append(9)
# print(x)
y = [10, 11, 12]
listOfLists = [x, y]
# print(listOfLists)
# print(y[1])
z = [3, 2, 1]
z.sort()
# print(z)
z.sort(reverse=True)
# print(z)
(age, income) = "32,120000".split(',')
# print(age)
# print(income)

# Like a map or hash table in other languages
captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janeway"

# print(captains["Voyager"])
# print(captains.get("Enterprise"))
# print(captains.get("NX-01"))

# for ship in captains:
#     print(ship + ": " + captains[ship])
def SquareIt(x):
    return x * x

# print(SquareIt(2))

#You can pass functions around as parameters
def DoSomething(f, x):
    return f(x)

# print(DoSomething(SquareIt, 3))

#Lambda functions let you inline simple functions
# print(DoSomething(lambda x: x * x * x, 3))
# print(1 == 3)
# print(True or False)
# print(1 is 3)
# if 1 is 3:
#     print("How did that happen?")
# elif 1 > 3:
#     print("Yikes")
# else:
#     print("All is well with the world")

# for x in range(10):
#     if (x is 1):
#         continue
#     if (x > 5):
#         break
    # print(x)
    
# x = 0
# while (x < 10):
#     print(x)
    # x += 1
    # print(x)
    
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(fr"C:\Users\vuqar\OneDrive\Documents\GitHub\python\practice\PastHires.csv")
# print(df.head(10))
# print(len(df))
# print(df.columns)
# print(df.shape)
# print(df.size)
# print(df["Hired"][:5])
# print(df["Hired"][5])
# print(df[["Years Experience", "Hired"]][:5])
# print(df.sort_values(["Years Experience"]))

# degree_counts = df['Level of Education'].value_counts()
# # print(degree_counts)
# # print(degree_counts.plot(kind='bar'))

# print(df[["Previous employers", "Hired"]][5:11])

# new_df = df[["Previous employers", "Hired"]][5:11]

# plt.figure(figsize=(8, 6))
# plt.hist(new_df['Previous employers'], bins=range(0, 8), edgecolor='black')
# plt.xlabel('Number of Previous Employers')
# plt.ylabel('Frequency')
# plt.title('Distribution of Previous Employers (Rows 5-10)')
# plt.xticks(range(0, 8))
# plt.show()



# incomes = np.random.normal(27000, 15000, 10000)
# # print(np.mean(incomes))
# plt.hist(incomes, 50)
# plt.show()

# incomes = np.random.normal(50.0, 10.0, 10000)
# incomes_with_outliers = np.append(incomes, [1000, 1200, 1500])
# mean_income = np.mean(incomes)
# median_income = np.median(incomes)

# print(f"Mean: {mean_income}")
# print(f"Median: {median_income}")
# plt.hist(incomes, 50)
# plt.show()

# incomes = np.random.normal(100.0, 20.0, 10000)
# print(incomes.std())
# print(incomes.var())
# plt.hist(incomes, 50)
# plt.show()

# values = np.random.uniform(-10.0, 10.0, 100000)
# plt.hist(values, 50)
# plt.show()

# from scipy.stats import norm
# from scipy.stats import expon
from scipy.stats import binom
# x = np.arange(-3, 3, 0.001)
# plt.plot(x, norm.pdf(x))
# plt.show()
# mu = 5.0
# sigma = 2.0
# values = np.random.normal(mu, sigma, 10000)
# plt.hist(values, 50)
# plt.show()


# x = np.arange(0, 10, 0.001)
# plt.plot(x, expon.pdf(x))


n, p = 10, 0.5
x = np.arange(0, 10, 0.001)
plt.plot(x, binom.pmf(x, n, p))