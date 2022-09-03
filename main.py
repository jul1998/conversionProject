from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(pady=20)

def calculate_miles_to_km():
    miles = float(entry_for_miles.get())
    km = miles * 1.6
    conversionLabel.config(text=km)

def listbox_used(event):
    # Gets current selection from listbox
    x = list_box.get(list_box.curselection())
    if x == "From Km to meters":
        print(True)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=10)

entry_for_miles = Entry(width=10)
entry_for_miles.grid(column=1, row=0)
entry_for_miles.focus()

miles = Label(text="Miles")
miles.grid(column=2, row=0)
miles.config(padx=10)

conversionLabel = Label(text=0)
conversionLabel.grid(column=1, row=1)
conversionLabel.config(pady=10)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

list_box = Listbox(height=3)
conversions = ["From miles to Km", "From Km to meters", "From Meters to cm"]
for item in conversions:
    list_box.insert(0, item)
list_box.grid(column=3, row=1)
list_box.bind("<<ListboxSelect>>", listbox_used)





calculate_button = Button(text="Calculate", command=calculate_miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()