from tkinter import *

window = Tk()
window.minsize(width=400, height=200)
window.config(padx=10, pady=10)

input = Entry(width=10)
input.insert(END, string='0')
input.grid(column=1, row=0)


window.mainloop()
