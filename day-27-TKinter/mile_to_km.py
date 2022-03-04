from tkinter import *

window = Tk()
window.title("Mile to Km converter")
# window.minsize(width=100, height=80)
# window.config(padx=50, pady=30)

def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    result.config(text=f"{km}")

#Labels
#my_label1 = Label(text="Miles", font=("Arial", 24, "bold"))
my_label1 = Label(text="Miles")
my_label1.grid(column=2, row=0)
my_label1.config(padx=5, pady=5)

my_label2 = Label(text="is equal to")
my_label2.grid(column=0, row=1)
my_label2.config(padx=5, pady=5)

my_label3 = Label(text="Km")
my_label3.grid(column=2, row=1)
my_label3.config(padx=5, pady=5)

result = Label(text="0")
result.grid(column=1, row=1)

#Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)











window.mainloop()