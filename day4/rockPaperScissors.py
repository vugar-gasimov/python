import random

print("\n Welcome to Rock Paper Scissors game.")
print("\n To Win the game: \n - 0 is Rock crushes Scissors (Rock wins) \n - 1 is Scissors cut Paper (Scissors win) \n - 2 is Paper covers Rock (Paper wins) \n Ties: If both players choose the same option, it's a tie.\n ")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_options = [rock, paper, scissors]

# users_points = 0
# computers_points = 0

user_choice = int(input(" What would you like to choose to play the game. 0 Rock, 1 Scissors, 2 Paper? "))
computer = random.randint(0, 2)
computer_move = game_options[computer]
user_move = game_options[user_choice]

if user_move == computer_move:
    print(f"\nYou chose: {user_move}")
    print(f"Computer chose: {computer_move}")
    print("It's a tie!")
elif (user_move == "rock" and computer_move == "scissors") or (user_move == "paper" and computer_move == "rock") or (user_move == "scissors" and computer_move == "paper"):
    print(f"\nYou chose: {user_move}")
    print(f"Computer chose: {computer_move}")
    print("You won!")
else:
    print(f"\nYou chose: {user_move}")
    print(f"Computer chose: {computer_move}")
    print("Computer won!")
# while True:
#     computer = random.randint(0, 2)
#     user_choice = int(input(" What would you like to choose to start game. 0 Rock, 1 Scissors, 2 Paper? "))
#     user_move = game_options[user_choice]
#     computer_move = game_options[computer]

#     print(f"\nYou chose: {user_move}")
#     print(f"Computer chose: {computer_move}")
#     if computer_move == user_move:
#        print(f"Results: Computer: {computers_points}, User: {users_points}.")
#        print("It's a tie!")
#     elif (user_choice == "rock" and computer_move == "scissors") or (user_choice == "scissors" and computer_move == "paper") or (user_choice == "paper" and computer_move == "rock"):
#        users_points =+ 1
#        print("User won 1 point!")
#        print(f"Results: Computer: {computers_points}, User: {users_points}.")
#     else:
#        computers_points =+ 1
#        print("Computer won 1 point!")
#        print(f"Results: Computer: {computers_points}, User: {users_points}.")
    
#     play_again = input("Do you want to play again? (y/n): ").lower()
#     if play_again != 'y':
#         break
    
print("\nThanks for playing!")