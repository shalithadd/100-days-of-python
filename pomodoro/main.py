import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
# noinspection PyTypeChecker
def reset_timer():
    try:
        root.after_cancel(timer)
        canvas.itemconfig(timer_text, text='00:00')
        lbl_title.config(text='Timer', fg=GREEN)
        lbl_check_marks.config(text='')
        global reps
        reps = 0
    except ValueError:
        print('Timer has not started.')


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_secs)
        lbl_title.config(text='Long Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        lbl_title.config(text='Break', fg=PINK)
    else:
        count_down(work_secs)
        lbl_title.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_mins = math.floor(count / 60)
    count_secs = count % 60
    # Display number of seconds with a leading 0 e.g. 09, 08
    if count_secs < 10:
        count_secs = f'0{count_secs}'

    canvas.itemconfig(timer_text, text=f'{count_mins}:{count_secs}')
    if count > 0:
        global timer
        timer = root.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_marks = ''
        work_sessions_completed = math.floor(reps / 2)
        for _ in range(work_sessions_completed):
            check_marks += '✔'
        lbl_check_marks.config(text=check_marks)


# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title('Pomodoro')
root.config(padx=100, pady=50, bg=YELLOW)

# Timer label
lbl_title = tk.Label(text='Timer', font=(FONT_NAME, 30, 'bold'), fg=GREEN, bg=YELLOW)
lbl_title.grid(pady=10, row=0, column=1)

# Tomato image
tomato_img = tk.PhotoImage(file='tomato.png')
canvas = tk.Canvas(width=200, height=224, bg=YELLOW)
canvas.create_image(102, 112, image=tomato_img)

# Timer on top of tomato image
timer_text = canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, 28, 'bold'))
canvas.grid(row=1, column=1)

# Start button
btn_start = tk.Button(text='Start', command=start_timer)
btn_start.grid(row=2, column=0)

# Reset button
btn_reset = tk.Button(text='Reset', command=reset_timer)
btn_reset.grid(row=2, column=2)

# Label to keep track of the number of laps
lbl_check_marks = tk.Label(font=(FONT_NAME, 12, 'normal'), bg=YELLOW, fg=GREEN)
lbl_check_marks.grid(row=3, column=1)

root.mainloop()
