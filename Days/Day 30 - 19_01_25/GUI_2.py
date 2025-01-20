from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()

ttk.Label(frm, text="Pop-up Box").grid(column=1, row=0)
ttk.Label(frm, text="This").grid(column=1, row=1)
ttk.Label(frm, text="Hello, Tkinter").grid(column=1, row=2)

ttk.Button(frm, text="Accept", command=root.destroy).grid(column=0, row=3)
ttk.Button(frm, text="Enquire", command=root.destroy).grid(column=1, row=3)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=3)
root.mainloop()