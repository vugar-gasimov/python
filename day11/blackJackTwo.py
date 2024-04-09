import art
import random

print("############### Blackjack Project ####################")
print("############### Our Blackjack House Rules #####################")
print("## The deck is unlimited in size. \n ## There are no jokers. \n ## The Jack/Queen/King all count as 10. \n ## The the Ace can count as 11 or 1. \n ## Use the following list as the deck of cards: \n ## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] \n ## The cards in the list have equal probability of being drawn. \n ## Cards are not removed from the deck as they are drawn. \n ## The computer is the dealer.")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """
    Returns a random card from the list of cards.
    """
    return random.choice(cards)
  
user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    



#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

