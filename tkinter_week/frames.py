import tkinter as tk 

root = tk.Tk()
root.title("frame demo")

frame = tk.Frame(root, bg = "lightblue", width=200, height=100, bd=3, relief=tk.RIDGE)
frame.pack(padx=10, pady=20)

label=tk.Label(frame, text="this is a frame", bg="lightblue")
label.pack(pady=20)

root.mainloop()