import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

# Access words in data.csv
data = pandas.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient='records')

root = tk.Tk()
root.title('Flash Cards')
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French')
    canvas.itemconfig(card_word, text=current_card["French"])


# Crate images of front and back of the flash card
card_front = tk.PhotoImage(file='images/card_front.png')
card_back = tk.PhotoImage(file='images/card_back.png')
canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_front)

# Place 'Title' and 'Word' on top of front or back of the card
card_title = canvas.create_text(400, 150, text='Title', font=(FONT_NAME, 35, 'italic'))
card_word = canvas.create_text(400, 300, text='Word', font=(FONT_NAME, 50, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Place buttons
img_cross = tk.PhotoImage(file='images/wrong.png')
btn_unknown = tk.Button(image=img_cross, highlightthickness=0, command=next_card)
btn_unknown.grid(row=1, column=0)

img_check = tk.PhotoImage(file='images/right.png')
btn_check = tk.Button(image=img_check, highlightthickness=0, command=next_card)
btn_check.grid(row=1, column=1)

next_card()

tk.mainloop()
