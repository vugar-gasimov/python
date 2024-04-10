import art
import random

print("             ############### Blackjack Project ##################")
print("          ############### Our Blackjack House Rules ##################")
print("\n ## The deck is unlimited in size. \n ## There are no jokers. \n ## The Jack/Queen/King all count as 10. \n ## The the Ace can count as 11 or 1. \n ## Use the following list as the deck of cards: \n ## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] \n ## The cards in the list have equal probability of being drawn. \n ## Cards are not removed from the deck as they are drawn. \n ## The computer is the dealer.")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """
    Returns a random card from the list of cards.
    """
    return random.choice(cards)

def play_game():
    """
    This function plays a game of Blackjack. It deals two cards each to the player and the computer. 
    Then, it allows the player to draw additional cards if they choose to. After the player is done drawing, 
    the computer draws cards until it reaches a score of 17 or higher. 
    Once both the player and the computer are done drawing cards, the function compares their scores to determine 
    the winner based on Blackjack rules. The player can choose to play again after the game ends.
    """
    
    print(art.logo)
    
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    def calculate_score(cards):
        """Take a list of cards and return the score calculated from the cards."""
        if sum(cards) == 21 and len(cards) == 2:
            return 0

        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
            
        return sum(cards)
        
   
    def compare(user_score, computer_score):
        """This function compares both scores User and Computer and based on game rules declares who is the winner"""
        if user_score == computer_score:
            return "Draw, It's a tie!" 
        elif user_score == 0:
            return "Blackjack. You win!"
        elif computer_score == 0:
            return "Blackjack. Computer wins!"
        elif user_score > 21:
            return "You Busted. Computer wins."
        elif computer_score > 21:
            return "Computer Busted. You win!"
        elif user_score > computer_score:
            return "You win."
        else:
            return "You lose."
        
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\n    Your cards: {user_cards}, current score: {user_score}. ")
        print(f"    Computer's first card: {computer_cards[0]}. \n")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_new_card = input("Would you like to add another card? (y/n): ")
            if user_new_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
        
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand is: {user_cards}, and your final score is: {user_score}. ")
    print(f"Computer's final hand is: {computer_cards}, and computer's final score is: {computer_score}. \n")
    print(compare(user_score, computer_score))
    new_game = input("\n Would you like to play again? (y/n): ")
    if new_game == "y":
        play_game()
    else:
        print("\n Thanks for playing. Goodbye.")

first_game = input("\n Would you like to play a game of blackjack? (y/n): ")
if first_game == "y":
    play_game()
else:
    print("\n Maybe next time.")
    