import pandas as pd
nato_data = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dic = {row.letter: row.code for index, row in nato_data.iterrows()}
input_word = input("Enter a word: ").upper()
answer = [nato_dic[letter] for letter in input_word if letter.isalpha()]
print(answer) 