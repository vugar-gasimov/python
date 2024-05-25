import pandas as pd

data = pd.read_csv(r"day26\Nato_alphabet\nato_phonetic_alphabet.csv")

dictionary = {row.letter:row.code for (index, row) in data.iterrows()}
# print(dictionary)
print("\nWelcome to Nato Phonetic Alphabet\n")
user_input = input("Enter a word: ").upper()
n_p_a_format = []
# for word in user_input:
#     n_p_a_format.append(dictionary[word])
n_p_a_format = [dictionary[word] for word in user_input]
#['Sierra', 'Alfa', 'Lima', 'Alfa', 'Mike']
print(f"\n {n_p_a_format} \n")