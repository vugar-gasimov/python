# enemies = 1 

# def increase_enemies():
#     enemies = 2
#     print(f"Enemies inside function {enemies}")
    
# increase_enemies()
# print(f"Enemies outside function {enemies}")

# output 2 than 1

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
    
# drink_potion()
# print(potion_strength)

# output 2 than error

# player_health = 10

# def drink_potion():
#     potion_strength = 2
#     print(player_health)
# drink_potion()
# output 10

# game_level = 3
# enemies = ["Skeleton","Alien","Zombie",]
# if game_level < 5:
#     new_enemy = enemies[0]
# print(new_enemy)
# output Skeleton

# enemies = 1

# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"Enemies inside function {enemies}")
    
# increase_enemies()
# print(f"Enemies outside function {enemies}")
enemies = 1

def increase_enemies():
    print(f"Enemies inside function {enemies}")
    return enemies + 1
    
enemies= increase_enemies()
print(f"Enemies outside function {enemies}")