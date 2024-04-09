
import art
import random

def greet_and_ask():
    """
    Greets the user and asks if they want to play Blackjack.
    """
    want_to_play = input("\n  Greetings would you like to play a game of Blackjack? Type 'y' or 'n': ")
    if want_to_play == "y":
        play_blackjack()
    else:
        print("Maybe next time. Goodbye!")
        
def play_blackjack():
    """
    Plays a game of Blackjack.
    """
    print("Welcome to BlackJack!") 
    print(art.logo)
   

    all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards = []
    computers_cards = []
    current_score = 0
    computers_current_score = 0
    
    for _ in range(2):
        random_number = random.choice(all_cards)
        cards.append(random_number)
        all_cards.remove(random_number)
    for _ in range(2):
        random_number = random.choice(all_cards)
        computers_cards.append(random_number)
        all_cards.remove(random_number)
     
    current_score = sum(cards)
    computers_current_score = sum(computers_cards)
    
        
    while current_score < 21:
        print(f"  Your cards: {cards}, current score: {current_score} ")
        print(f"  Computer's first card: {computers_cards[0]} ")
        to_get_card = input("Type 'y' to get another card, type 'n' to pass: ")
        
        if to_get_card == "y":
            random_number = random.choice(all_cards)
            cards.append(random_number)
            all_cards.remove(random_number)
            current_score = sum(cards)
        else:
            break
        
    while computers_current_score < 17:
        random_number = random.choice(all_cards)
        computers_cards.append(random_number)
        all_cards.remove(random_number)
        computers_current_score = sum(computers_cards)
        
    print(f"  Your final hand: {cards}, final score: {current_score} ")
    print(f"  Computer's final hand: {computers_cards}, final score: {computers_current_score} ")

    if current_score == 21:
        print("     BlackJack! You win!")
    elif current_score > 21:
        print("     Busted! You lose!")
    elif computers_current_score == 21:
        print("     Computer got BlackJack! You lose!")
    elif computers_current_score > 21:
        print("     Computer Busted! You win!")
    elif current_score > computers_current_score:
        print("     You win!")
    elif current_score < computers_current_score:
        print("     You lose!")
    else:
        print("     It's a draw!")
    ask_play_again()

def ask_play_again():
    """
    Asks the user if they want to play again.
    """
    play_again = input("Would you like to play again? Type 'y' for yes and 'n' for no: ")[0].lower()
    if play_again == "y":
        play_blackjack()
    else:
        print("Thanks for playing. Goodbye.")
        
greet_and_ask()