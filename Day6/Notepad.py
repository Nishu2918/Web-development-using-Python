import tkinter as tk

root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

format_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Format", menu=format_menu)

root.config(menu=menu_bar)

text_area = tk.Text(root)
text_area.pack(expand=True, fill=tk.BOTH)

root.mainloop()
