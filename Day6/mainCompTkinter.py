import tkinter as tk

root = tk.Tk()
root.title("Main Components Example")

frame = tk.Frame(root, bg="lightgray", bd=2, relief=tk.SUNKEN)
frame.pack(padx=50, pady=50)

label = tk.Label(frame, text="This is a label")
label.pack(padx=10, pady=10)

button = tk.Button(frame, text="This is a button")
button.pack(padx=5, pady=5)

root.mainloop()