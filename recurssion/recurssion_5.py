from tkinter import *

counter = 0

def count():
    global counter
    counter += 1
    lbl.config(text=counter)
    root.after(10, count)

root = Tk()
lbl = Label(root, text='0')
lbl.pack()
Button(root, text='Start count', command=count).pack()
Button(root, text='stop count', command=root.destroy).pack()
root.mainloop()