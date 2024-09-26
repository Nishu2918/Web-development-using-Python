import tkinter as tk

root = tk.Tk()
root.title("Example of Listbox")

listbox = tk.Listbox(root)
listbox.pack()

listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.insert(3, "Item 3")
root.mainloop()