from tkinter import * 

window = Tk()

r = Label(bg="red", width=20, height=5)
r.grid(row=0, column=0)

r = Label(bg="green", width=20, height=5)
r.grid(row=1, column=1)

r = Label(bg="blue", width=40, height=5)
r.grid(row=2, column=0, columnspan=2)
# columnspan is mean to make column longer than usual column
# In this exmaple its will be longer on 2 times! 


window.mainloop()
