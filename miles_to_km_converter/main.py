import tkinter as tk

root = tk.Tk()
root.minsize(width=300, height=100)
root.title('Miles to Km Converter')
root.config(pady=20, padx=20)


def calculate_km():
    miles = float(user_input.get())
    km = round(miles * 1.609344, 2)
    lbl_output.config(text=km)


user_input = tk.Entry(root, width=10)
user_input.grid(column=1, row=0)
user_input.focus()

lbl_miles = tk.Label(root, text='Miles')
lbl_miles.grid(column=2, row=0)

lbl_is_equal_to = tk.Label(root, text='is equal to')
lbl_is_equal_to.grid(column=0, row=1)

lbl_output = tk.Label(root, text='')
lbl_output.grid(column=1, row=1)

lbl_km = tk.Label(root, text='Km')
lbl_km.grid(column=2, row=1)

btn_calculate = tk.Button(root, text='Calculate', command=calculate_km)
btn_calculate.grid(column=1, row=2)
root.mainloop()
