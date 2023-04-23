import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title('Pomodoro')
root.config(padx=100, pady=50, bg=YELLOW)

tomato_img = tk.PhotoImage(file='tomato.png')
canvas = tk.Canvas(width=200, height=224, bg=YELLOW)
canvas.create_image(102, 112, image=tomato_img)
canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, 28, 'bold'))
canvas.pack()

root.mainloop()
