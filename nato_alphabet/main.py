import pandas

# Create a dict form 'nato_phonetic_alphabet.csv'
df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic_letters():
    word = input('Enter a word: ').upper()
    try:
        result = [nato_alphabet[letter] for letter in word]
    except KeyError:
        print('Please enter a letter in the alphabet.')
        generate_phonetic_letters()
    else:
        print(result)


generate_phonetic_letters()
