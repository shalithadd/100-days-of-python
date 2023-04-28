import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title('Password Manager')
root.config(pady=30, padx=30)

logo = tk.PhotoImage(file='logo.png')
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

lbl_website = tk.Label(text='Website:', font=('Arial', 12, 'normal'))
lbl_website.grid(row=1, column=0)

entry_website = tk.Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2)

lbl_email = tk.Label(text='Email/Username:', font=('Arial', 12, 'normal'))
lbl_email.grid(row=2, column=0)

entry_email = tk.Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2)

lbl_password = tk.Label(text='password:', font=('Arial', 12, 'normal'))
lbl_password.grid(row=3, column=0)

entry_password = tk.Entry(width=17)
entry_password.grid(row=3, column=1)

btn_generate_password = tk.Button(text='Generate Password')
btn_generate_password.grid(row=3, column=2)

btn_add = tk.Button(text='Add', width=30)
btn_add.grid(row=4, column=1, columnspan=2)
root.mainloop()
