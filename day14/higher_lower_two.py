from art import logo, vs
import random
import game_data 

def format_data(celebrity):
    """Takes celebrity data and returns printable format."""
    name = celebrity["name"]
    description = celebrity["description"]
    country = celebrity["country"]
   
    return f"{name}, is a {description}, from {country}"

def check_answer(guess, a_follower, b_follower):
    """Takes user's guess and checks follower count and returns if they got it right"""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(game_data.data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(game_data.data)

    while account_a == account_b:
        account_b = random.choice(game_data.data)
        
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? (A/B): ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Your current score is {score}.")
    else:
        print(f"Sorry, that's wrong! Your final score is {score}.")
        game_should_continue = False