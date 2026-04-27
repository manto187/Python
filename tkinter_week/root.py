from tkinter import *

root = Tk()
root.title("hello world")
root.geometry('350x200')

root.mainloop()


# label inside root window

# from tkinter import *

# root = Tk()

# root.title("weclome to python")
# root.geometry('350x200')

# label = Label(root, txt = "are you a developer?")
# label.grid()
# root.mainloop()



# adding button
from tkinter import *

root = Tk()
root.title("weclome to python")
root.geometry('350x200')

label = Label(root, text = "are you a developer?")
label.grid()

def clicked():
    label.configure(text = "im just a developer")

btn = Button(root, text = "hire me", 
             fg = "blue", command = clicked)

btn.grid(column = 1, row=0)

root.mainloop()