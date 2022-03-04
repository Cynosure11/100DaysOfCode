from tkinter import *

window = Tk()
window.title("My first Graphic User Interface")
window.minsize(width=500, height=300)

window.config(padx=100, pady=200)
# window.config(text=new_text)

# Label

# You can use "Type: Arial, Times new roman", "Size:1- 100"
# "And type word:Bold, Italic, Underline"
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button

# Found from stackoverflow
# don't forget to import module # import tkinter.messagebox
# def callback():
#    tkinter.messagebox.showinfo("", "Hey sun of bitch")
# button = Button(window, text="If you are bitch", command=callback)

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# button2
button2 = Button(text="New Button", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)


window.mainloop()
