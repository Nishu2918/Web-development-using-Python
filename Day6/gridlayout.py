import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

label = tk.Label(root, text="Label 1", bg="red")
label.grid(row=0, column=0)

label2 = tk.Label(root,text="Label 2", bg="blue")
label2.grid(row=1, column=1)

root.mainloop()