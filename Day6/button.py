import tkinter as tk

root = tk.Tk()
root.title("Button")
root.geometry("400x300")

def filer():
    label.config(text="file button is clicked")

def editr():
    label.config(text="edit button is clicked")

def saver():
    label.config(text="save button is clicked")

def viewer():
    label.config(text="view button is clicked")

def go_back_opt():
    label.config(text="go back button is clicked")

label = tk.Label(root,text="click an item")
label.grid(row=10,column=10)

button = tk.Button(root,text="file", command=filer)
button.grid(row=1,column=1)

button = tk.Button(root,text="edit", command=editr)
button.grid(row=1,column=2)

button = tk.Button(root,text="save", command=saver)
button.grid(row=1,column=3)

button = tk.Button(root,text="view", command=viewer)
button.grid(row=1,column=4)

button = tk.Button(root,text="go back", command=go_back_opt)
button.grid(row=1,column=5)

root.mainloop()
