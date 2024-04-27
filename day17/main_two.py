class User:
    # pass
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("New user being created...")
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_one = User("0", "Gasimov")
# user_one.id = "1000"
# user_one.username = "Gasimov"

user_two = User("1", "Ibrahimov")
# user_two.id = "1001"
# user_two.username = "Ibrahimov"

user_one.follow(user_two)
print(user_one)
print(user_one.followers)
print(user_one.following)
print(user_two.username)
print(user_two.followers)
print(user_two.following)

# class Car:
#     def enter_race_mode(self):
#         self.seats = 2
#         print("Entering race mode")

# my_car = Car() 
# my_car.enter_race_mode()


# text = "2+3=5"
# answer = True

# new_q = Question("2+3=5", True)