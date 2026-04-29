import tkinter as tk

root = tk.Tk()
lbl = tk.Label(root, text="Hello World")
lbl.pack()

root.mainloop()


import tkinter as tk

root = tk.Tk()
root.geometry("400x200")
root.title("Label Example")

lbl = tk.Label(root,
               text="Welcome to Tkinter",
               font=("Arial", 16, "bold"),
               bg="lightblue",
               fg="darkblue",
               width=20,
               height=2,
               relief="raised")

lbl.pack(pady=30)
root.mainloop()