import tkinter as tk
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

root = tk.Tk()
root.title('Flash Cards')
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Crate images of front and back of the flash card
card_front = tk.PhotoImage(file='images/card_front.png')
card_back = tk.PhotoImage(file='images/card_back.png')
canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_front)

# Place 'Title' and 'Word' on top of front or back of the card
canvas.create_text(400, 150, text='Title', font=(FONT_NAME, 35, 'italic'))
canvas.create_text(400, 300, text='Word', font=(FONT_NAME, 50, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Place buttons
img_right = tk.PhotoImage(file='images/right.png')
img_wrong = tk.PhotoImage(file='images/wrong.png')
btn_wrong = tk.Button(image=img_wrong, highlightthickness=0)
btn_wrong.grid(row=1, column=0)
btn_right = tk.Button(image=img_right, highlightthickness=0)
btn_right.grid(row=1, column=1)


tk.mainloop()
