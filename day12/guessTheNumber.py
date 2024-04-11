import art
import random
def GuessNumber():
    """Guess a Number Game
    This game will ask the user to guess a number between 1 and 100. The computer will then give hints about whether the number high or low and will show user how many attempts they have left based on their difficulty.
    """
    print(art.logo)
    print(" >>>>>>>>>>>>> Welcome to the Number Guessing Game! <<<<<<<<<<<<<<<<<<< \n")
    print("I'm thinking of a number between 1 and 100. \n")
    computer_thinking = random.randint(1, 100)

    # remove in the end and update
    # print(f"Psst, the correct answer is {computer_thinking}")
    difficulty = input("Choose a difficulty. Type (hard/easy): ").lower()
    if difficulty == "hard":
        attempts = 5
        print(">You have 5 attempts to guess the number.\n")
    else:
        attempts = 10
        print(">You have 10 attempts to guess the number.\n")
    # update
    while attempts > 0: 
        user_guess = int(input("Make a guess: "))
        won = False
        if user_guess == computer_thinking:
            print(f"You got it! The answer was {user_guess}.")
            attempts = 0
            won = True
        elif user_guess > computer_thinking:
            print(" >>Too high.")
            attempts -= 1
            if attempts > 0:
                print(" Guess again.")
                print(f">You have {attempts} attempts to guess the number. \n")
        else:  
            print(" >>Too low.")
            attempts -= 1
            if attempts > 0:
                print(" Guess again.")
                print(f">You have {attempts} attempts to guess the number. \n")
            
        if attempts == 0 and won == False:
            print("  You've run out of guesses, you lose.")
            
    play_again = input("\n   Would you like to play again ? (y/n): ")[0].lower()
    if play_again == "y":
        GuessNumber()
    else:
        print("\n  Thanks for playing. Goodbye.")
            
        
play = input("\n     > Would you like to play a game named >Guess a Number< ? (y/n): ")[0].lower()
if play == "y":
    GuessNumber()
else:
    print("\n  Maybe next time. Goodbye.")