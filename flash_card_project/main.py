import random
import tkinter as tk

import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

try:
    data = pandas.read_csv('data/words_to_learn.csv')
    to_learn = data.to_dict(orient='records')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
    to_learn = data.to_dict(orient='records')

current_card = {}


def known_word():
    global current_card
    to_learn.remove(current_card)
    updated_words = pandas.DataFrame.from_records(to_learn)
    updated_words.to_csv('data/words_to_learn.csv', index=False)
    next_card()


def next_card():
    global current_card, flip_timer
    root.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card["French"], fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = root.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')
    canvas.itemconfig(card_background, image=card_back_img)


root = tk.Tk()
root.title('Flash Cards')
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = root.after(3000, flip_card)

# Crate images of front and back of the flash card
card_front_img = tk.PhotoImage(file='images/card_front.png')
card_back_img = tk.PhotoImage(file='images/card_back.png')
canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_background = canvas.create_image(400, 263, image=card_front_img)

# Place 'Title' and 'Word' on top of front or back of the card
card_title = canvas.create_text(400, 150, text='Title', font=(FONT_NAME, 35, 'italic'))
card_word = canvas.create_text(400, 300, text='Word', font=(FONT_NAME, 70, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Place buttons
img_cross = tk.PhotoImage(file='images/wrong.png')
btn_unknown = tk.Button(image=img_cross, highlightthickness=0, command=next_card)
btn_unknown.grid(row=1, column=0)

img_check = tk.PhotoImage(file='images/right.png')
btn_check = tk.Button(image=img_check, highlightthickness=0, command=known_word)
btn_check.grid(row=1, column=1)
next_card()

tk.mainloop()
