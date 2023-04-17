# Get names form the file invited_names and save to invited_name list
with open('./input/Names/invited_names.txt', mode='r') as f:
    contents = f.readlines()
invited_names = []
for name in contents:
    invited_names.append(name.strip())

# Get the latter from the file starting_letter and save as text string
with open('./input/Letters/starting_letter.txt', mode='r') as f:
    text = f.read()

# For each name in invited_names list replace [name] in the text string and save as new_text
# Create new files in ReadyToSend folder and write new text
for name in invited_names:
    with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as f:
        new_text = text.replace('[name]', name)
        f.write(new_text)
