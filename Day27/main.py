from tkinter import *

def miles_to_km():
    calc_num = float(num_miles.get()) * 1.609
    answer_label.config(text=round(calc_num, 2))

window = Tk()
window.title("Miles to km")
window.config(padx=20, pady=20)

miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

km_label = Label(text="KM", font=("Arial", 12))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

equal_label = Label(text="Equals", font=("Arial", 12))
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

answer_label = Label(text=0, font=("Arial", 12))
answer_label.grid(column=1, row=1)
answer_label.config(padx=10, pady=10)

num_miles = Entry(width=10, font=("Arial", 12))
num_miles.grid(column=1, row=0)

calculate_button = Button(text="Calculate", command=miles_to_km, font=("Arial", 12))
calculate_button.grid(column=1, row=2)

window.mainloop()