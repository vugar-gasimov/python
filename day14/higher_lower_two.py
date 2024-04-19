import art
import random
import game_data 

print(art.logo)

account_a = random.choice(game_data.data)
account_b = random.choice(game_data.data)

if account_a == account_b:
    account_a = random.choice(game_data.data)