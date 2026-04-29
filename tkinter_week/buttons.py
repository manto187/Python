import tkinter as tk

def button_clicked():
    print("Button clicked!")

root = tk.Tk()

button = tk.Button(root, 
                   text="Click Me", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button.pack(padx=20, pady=20)

root.mainloop()



# creation of buttons without using TK themed widget

from tkinter import *         
from tkinter.ttk import *

root = Tk()           
root.geometry('100x100')     

btn = Button(root, text = 'Click me !', 
                command = root.destroy) 

btn.pack(side = 'top')     

root.mainloop()