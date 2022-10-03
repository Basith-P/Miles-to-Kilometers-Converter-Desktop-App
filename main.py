from tkinter import *

window = Tk()
window.title("Miles to KMs Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Entry
miles_entry = Entry(width=7)
miles_entry.grid(column=1, row=0)

# Button


def button_clicked():
    miles = float(miles_entry.get())
    km = miles * 1.609
    km_value.config(text=f"{km}")


button = Button(text="Calculate", command=button_clicked)
button.grid(column=3, row=0)

# Label
km_value = Label(text="0")
km_value.grid(column=1, row=1)

# Label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

window.mainloop()
