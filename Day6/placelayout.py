import tkinter as tk

root = tk.Tk()
root.title("Testing place layout")
root.geometry("300x200")

label = tk.Label(root, text="Label 1", bg="red")
label.place(x=50, y=50)

label2 = tk.Label(root,text="Label 2", bg="blue")
label2.place(x=150, y=100)

root.mainloop()