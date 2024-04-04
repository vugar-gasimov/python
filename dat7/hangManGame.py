import random
import hangman_art
import hangman_words
print(hangman_art.logo)
print("\n        Welcome to hangman game! \n")
chosen_level = input("Please choose a level like 'easy', 'medium', 'hard' or random names) ")

if chosen_level == "easy":
    random_word = random.choice(hangman_words.easy_word_list).lower() 
elif chosen_level == "medium":
    random_word = random.choice(hangman_words.medium_word_list).lower() 
elif chosen_level == "hard":
    random_word = random.choice(hangman_words.hard_word_list).lower()
else:
     random_word = random.choice(hangman_words.random_names).lower()

random_word_len = len(random_word)
display = ["_"] * random_word_len
lives = 6
print(display)
print(random_word)

while True:
# while not end_of_game:
    guessed_word = input(f"\n You've {lives} lives. Guess a word: ").lower()[0]
    found = False
    
    if guessed_word in display:
        print(f"You've already guessed '{guessed_word}'.") 
        found = True
    else:
        for position in range(random_word_len):
            letter = random_word[position]
            if letter == guessed_word:
                print(f"\n You guessed '{guessed_word}', that's in the word.")
                display[position] = letter
                found = True
           
    
            
    print(display)
    
    if not found:
        print(f"\n You guessed '{guessed_word}', that's not in the word. You lose a life.")
        lives -= 1
        print(hangman_art.stages[lives])
    # Teacher's way
    # if guess not in chosen_word:
    #   lives -= 1
    #   if lives == 0:
    #       end_of_game = True
    #       print("You lose.")
            
    if display == list(random_word):
        print(f"{' '.join(display)}")
        print("Congratulations, you won! \n")
        break
    if lives == 0:
        print("Unfortunately you lost! \n")
        break
    # Teacher's way
    # if "_" not in display:
    #   end_of_game = True
    #   print("You win.")
    
