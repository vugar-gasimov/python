import art
import random
import game_data 

answer = True

def random_star():
    return random.choice(game_data.data)


print(art.logo)
while answer:
    random_star_a = random_star()
    random_star_b = random_star()
    current_score = 0 
    
    print(f"Compare A: {random_star_a['name']}, is a {random_star_a['description']}, from {random_star_a['country']}.")
    print(art.vs)
    print(f"Compare B: {random_star_b['name']}, is a {random_star_b['description']}, from {random_star_b['country']}.")
    
    user_answer = input("Who has more followers? (A/B): ").lower()
    if random_star_a['follower_count'] > random_star_b['follower_count']:
        a_is_higher = True
        b_is_higher = False
    else:
        a_is_higher = False
        b_is_higher = True
        
    if user_answer == "a" and a_is_higher == True:
        current_score += 1
        print(art.logo)
        print(f"You're right! Your current score is: {current_score}")
    elif user_answer == "b" and b_is_higher == True:
        current_score += 1
        print(art.logo)
        print(f"You're right! Your current score is: {current_score}")
    else:
        print(art.logo)
        print(f"Sorry, that's wrong your current score is: {current_score}")
        answer = False
        