import tkinter as tk

from numpy import var 

def on_button_click():
    if var.get() == 1:
        print("checkbutton is selected")
    else:
        print("checkbutton is not selected")

root = tk.Tk()
var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="enable feature", variable = var, 
                             onvalue=1, offvalue=0, command=on_button_click)
checkbutton.config(bg="lightgray", fg="blue", font=("Arial", 12),
                   selectcolor="green", relief="raised", padx=10, pady=5)

checkbutton.config(bitmap="info", width=20, height=2)
checkbutton.pack(padx=40,pady=40)
checkbutton.flash()

root.mainloop()