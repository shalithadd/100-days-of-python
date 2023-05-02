import tkinter as tk


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    with open('data.txt', 'a') as f:
        f.write(f'{website} | {email} | {password}\n')

    entry_website.delete(0, 'end')
    entry_password.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title('Password Manager')
root.config(pady=70, padx=70)

logo = tk.PhotoImage(file='logo.png')
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
lbl_website = tk.Label(text='Website:  ', font=('Arial', 12, 'normal'))
lbl_website.grid(row=1, column=0)
lbl_email = tk.Label(text='Email/Username:  ', font=('Arial', 12, 'normal'))
lbl_email.grid(row=2, column=0)
lbl_password = tk.Label(text='password:  ', font=('Arial', 12, 'normal'))
lbl_password.grid(row=3, column=0)

# Entries
entry_website = tk.Entry(width=52)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()
entry_email = tk.Entry(width=52)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, 'shalithadp@gmail.com')
entry_password = tk.Entry(width=34)
entry_password.grid(row=3, column=1)

# Buttons
btn_generate_password = tk.Button(text='Generate Password')
btn_generate_password.grid(row=3, column=2)
btn_add = tk.Button(text='Add', width=44, command=save)
btn_add.grid(row=4, column=1, columnspan=2)
root.mainloop()
