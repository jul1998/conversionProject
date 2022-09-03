# Conversion program using Tkinter

from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(pady=20)

def calculate_miles_to_km():
    from_unit.config(text= "Miles")
    to_unit.config(text="Km")
    miles = float(user_entry.get())
    km = round(miles * 1.6)
    conversionLabel.config(text=km)
    from_unit.focus()

def calculate_km_to_meters():
    from_unit.config(text="Km")
    to_unit.config(text="M")
    km = float(user_entry.get())
    m = round(km * 1000)
    conversionLabel.config(text=m)

def calculate_meters_to_cm():
    from_unit.config(text="M")
    to_unit.config(text="Cm")
    m = float(user_entry.get())
    cm = round(m * 100)
    conversionLabel.config(text=cm)


def listbox_event(event):
    # Gets current selection from listbox
    x = list_box.get(list_box.curselection())
    if x == "From Km to meters":
        if user_entry.get() != "":
            calculate_km_to_meters()
    elif x == "From Meters to cm":
        if user_entry.get() != "":
            calculate_meters_to_cm()
    else:
        if user_entry.get() != "":
            calculate_miles_to_km()


def reset():
    user_entry.delete(first=0, last=10)

user_entry = Entry(width=10)
user_entry.grid(column=1, row=0)
user_entry.focus()

from_unit = Label(text="Miles")
from_unit.grid(column=2, row=0)
from_unit.config(padx=10)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=10)

conversionLabel = Label(text=0)
conversionLabel.grid(column=1, row=1)
conversionLabel.config(pady=10)

to_unit = Label(text="Km")
to_unit.grid(column=2, row=1)



calculate_button = Button(text="Delete", command=reset)
calculate_button.grid(column=1, row=2)

list_box = Listbox(height=3)
conversions = ["From miles to Km", "From Km to meters", "From Meters to cm"]
for item in conversions:
    list_box.insert(0, item)
list_box.grid(column=3, row=1)
list_box.bind("<<ListboxSelect>>", listbox_event)


window.mainloop()