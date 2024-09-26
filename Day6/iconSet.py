import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()

root.title("My Tkinter App")

icon = PhotoImage(file=r'C:/Users/nisha/OneDrive/Desktop/Python web developer/Day6/Image.png')

root.iconphoto(True, icon)

root.geometry("400*300")
root.mainloop()