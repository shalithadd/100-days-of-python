import pandas

# Create a dict form 'nato_phonetic_alphabet.csv'
df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet = {row.letter: row.code for letter, row in df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
word = list(input('Enter a word: ').upper())
result = [nato_alphabet[char] for char in word if char in
          nato_alphabet.keys()]
print(result)
