import tkinter as tk

root = tk.Tk()
root.title("5 button program")
root.geometry("400x400")

label = tk.Label(root,text="This is a label",bg="cyan")
buttton = tk.Label(root,text='click me')
entry = tk.Entry(root)
text = tk.Text(root,height=5,width=30)
check_button = tk.Checkbutton(root,text="check me")
radio_button1 = tk.Radiobutton(root,text="option 1",value=1)
radio_button2 = tk.Radiobutton(root,text="option 2",value=2)

label.grid(row=0,column=0,padx=10,pady=10,sticky="w")
buttton.grid(row=0,column=1,padx=10,pady=10,sticky="e")
entry.grid(row=1,column=0,padx=10,pady=10,columnspan=2,sticky="ew")
text.grid(row=2,column=0,padx=10,pady=10,columnspan=2,sticky="ew")
check_button.grid(row=3,column=0,padx=10,pady=10,sticky="w")
radio_button1.grid(row=3,column=1,padx=10,pady=10,sticky="e")
radio_button2.grid(row=4,column=1,padx=10,pady=10,sticky="e")


root.grid_columnconfigure(index=0,weight=1)
root.grid_columnconfigure(index=1,weight=1)

root.mainloop()
