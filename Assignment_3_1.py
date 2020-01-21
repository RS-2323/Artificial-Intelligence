import numpy as np
import tkinter as tk

root=tk.Tk()
root.title("Chess board")
for i in range(0,8):
    for j in range(0,8):
        if(i%2==0):
            if(j%2!=0):
                tk.Button(root,bg="black",width=5,height=2).grid(row=i,column=j)
            else:
                tk.Button(root,bg="white",width=5,height=2).grid(row=i,column=j)
        else:
            
            if(j%2==0):
                tk.Button(root,bg="black",width=5,height=2).grid(row=i,column=j)
            else:
                tk.Button(root,bg="white",width=5,height=2).grid(row=i,column=j)
root.mainloop()
            