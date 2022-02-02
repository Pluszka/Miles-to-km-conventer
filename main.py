from tkinter import *

BLUE = '#5F758E'
YELLOW = '#DBDFAC'
DARKER_BLUE = '#383961'

def convert():
    km = int(user_input.get()) * 1.61
    output.config(text=km)


window = Tk()
window.minsize(width=200, height=100)
window.config(padx=10, pady=10, bg=DARKER_BLUE)
window.title(string='Miles to Km')

user_input = Entry(width=10, bg=BLUE, fg=YELLOW)
user_input.insert(END, string='0')
user_input.grid(column=1, row=0)

label1 = Label(text='miles', bg=DARKER_BLUE, fg=YELLOW)
label1.grid(column=2, row=0)

label2 = Label(text='is equal to', bg=DARKER_BLUE, fg=YELLOW)
label2.grid(column=0, row=1)

output = Label(width=8, fg=YELLOW, bg=BLUE)
output.grid(column=1, row=1)

label3 = Label(text='km', bg=DARKER_BLUE, fg=YELLOW)
label3.grid(column=2, row=1)

button = Button(text='Convert', width=10, command=convert, bg=YELLOW, fg=BLUE)
button.grid(column=1, row=2)

window.mainloop()
