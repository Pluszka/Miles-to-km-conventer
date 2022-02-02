from tkinter import *


def convert():
    km = int(user_input.get()) * 1.61
    output.config(text=km)


window = Tk()
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)
window.title(string='Miles to Km')

user_input = Entry(width=10)
user_input.insert(END, string='0')
user_input.grid(column=1, row=0)

label1 = Label(text='miles')
label1.grid(column=2, row=0)

label2 = Label(text='is equal to')
label2.grid(column=0, row=1)

output = Label(width=10)
output.grid(column=1, row=1)

label3 = Label(text='km')
label3.grid(column=2, row=1)

button = Button(text='Convert', width=10, command=convert)
button.grid(column=1, row=2)

window.mainloop()
