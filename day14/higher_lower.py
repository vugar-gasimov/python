import art
import random
from game_data import data

def output_info(celebrity):
    """Returns a tuple containing the celebrity's name, description, country, and follower count."""
    name = celebrity["name"]
    description = celebrity["description"]
    country = celebrity["country"]
    follower = celebrity["follower_count"]
    return name, description, country, follower

answer = True

print(art.logo)
random_star_a = random.choice(data)
random_star_b = random.choice(data)
current_score = 0 



a = output_info(random_star_a)
b = output_info(random_star_b)
while answer:
    is_same_celebrity = random_star_a == random_star_b  
    while is_same_celebrity:  
        random_star_b = random.choice(data)
        is_same_celebrity = random_star_a == random_star_b
    
    print(f"Compare A: {a[0]}, is a {a[1]}, from {a[2]}.")
    print(art.vs)
    print(f"Compare B: {b[0]}, is a {b[1]}, from {b[2]}.")
    
    user_answer = input("Who has more followers? (A/B): ").lower()
    if a[3] > b[3]:
        a_is_higher = True
        b_is_higher = False
    else:
        a_is_higher = False
        b_is_higher = True
        
    if user_answer == "a" and a_is_higher == True:
        current_score += 1
        random_star_a = random_star_a
        random_star_b = random.choice(data)
        print(art.logo)
        print(f"You're right! Your current score is: {current_score}")
    elif user_answer == "b" and b_is_higher == True:
        current_score += 1
        random_star_a = random_star_b
        random_star_b = random.choice(data)
        print(art.logo)
        print(f"You're right! Your current score is: {current_score}")
    else:
        print(art.logo)
        print(f"Sorry, that's wrong your current score is: {current_score}")
        answer = False
        