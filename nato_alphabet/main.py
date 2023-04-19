import pandas

# Create a dict form 'nato_phonetic_alphabet.csv'
df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
word = input('Enter a word: ').upper()
result = [nato_alphabet[letter] for letter in word]
print(result)
