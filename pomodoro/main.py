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
# Timer label
lbl_timer = tk.Label(text='Timer', font=(FONT_NAME, 30, 'bold'), fg=GREEN, bg=YELLOW)
lbl_timer.grid(pady=10, row=0, column=1)
# Tomato image
tomato_img = tk.PhotoImage(file='tomato.png')
canvas = tk.Canvas(width=200, height=224, bg=YELLOW)
canvas.create_image(102, 112, image=tomato_img)
# Timer on top of tomato image
canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, 28, 'bold'))
canvas.grid(row=1, column=1)

# Start button
btn_start = tk.Button(text='Start')
btn_start.grid(row=2, column=0)

# Reset button
btn_reset = tk.Button(text='Reset')
btn_reset.grid(row=2, column=2)

# Label to keep track of the number of laps
lbl_check_marks = tk.Label(text='✔', font=(FONT_NAME, 12, 'normal'), bg=YELLOW, fg=GREEN)
lbl_check_marks.grid(row=3, column=1)

root.mainloop()
