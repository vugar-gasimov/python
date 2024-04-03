import random

print("\n        Welcome to hangman game! \n")
# chosen_level = input("Please choose a level like 'easy', 'medium', or hard' ")
easy_word_list = ["Smile",
"Donut",
"Beach",
"Jeans",
"Whisper",
"Melody"]
medium_word_list = ["Rainbow",
"Butterfly",
"Costume",
"Bicycle",
"Champion",
"Mystery"]
hard_word_list = ["Magnificent",
"Nevertheless",
"Equilibrium",
"Orchestra",
"Archipelago",
"Silhouette"]
random_word = random.choice(easy_word_list).lower()
random_word_len = len(random_word)
display = ["_"] * random_word_len
print(display)
guessed_word = input("\n Guess a word: ").lower()
updated_display= []
for letter in random_word:
    
    if letter == guessed_word:
        print(True)
        updated_display += letter
    else:
        print(False)
        updated_display += '_'
print(updated_display)