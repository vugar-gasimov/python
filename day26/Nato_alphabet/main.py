# import pandas as pd

# data = pd.read_csv(r"day26\Nato_alphabet\nato_phonetic_alphabet.csv")

# dictionary = {row.letter:row.code for (index, row) in data.iterrows()}
# # print(dictionary)
# print("\nWelcome to Nato Phonetic Alphabet\n")
# work = True
# while work:
#     user_input = input("Enter a word: ").upper()
#     n_p_a_format = []
#     # for word in user_input:
#     #     n_p_a_format.append(dictionary[word])
#     try:
#         n_p_a_format = [dictionary[word] for word in user_input]
#     except KeyError:
#         print("\n Sorry, only letters in the alphabet please.\n")
#     else:
#         print(f"\n {n_p_a_format} \n")
#         work = False
#     #['Sierra', 'Alfa', 'Lima', 'Alfa', 'Mike']

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import pandas as pd

data = pd.read_csv(r"day26\Nato_alphabet\nato_phonetic_alphabet.csv")

dictionary = {row.letter:row.code for (index, row) in data.iterrows()}
# print(dictionary)
print("\nWelcome to Nato Phonetic Alphabet\n")

def generate_phonetics():
    user_input = input("Enter a word: ").upper()
    # n_p_a_format = []
    # for word in user_input:
    #     n_p_a_format.append(dictionary[word])
    try:
        n_p_a_format = [dictionary[word] for word in user_input]
    except KeyError:
        print("\n Sorry, only letters in the alphabet please.\n")
        generate_phonetics()
    else:
        print(f"\n {n_p_a_format} \n")
        
    #['Sierra', 'Alfa', 'Lima', 'Alfa', 'Mike']
generate_phonetics()