import numpy as np
import tkinter as tk

root=tk.Tk()
root.title("MAGIC SQUARE")
tk.Label(root,text="Enter the value of magic square>").grid(row=0,column=0)
enter=tk.Entry(root)
enter.grid(row=0,column=1)
def matrix_generator():
    global enter
    N=(int(str(enter.get())))
    magic_square=np.zeros((N,N),dtype=int)
    n=1
    i,j=0,N//2
    while n<N*N:
        magic_square[i,j]=n
        n=n+1
        newi,newj=(i-1)%N,(j+1)%N
        if magic_square[newi,newj]:
            i=i+1
        else:
            i,j=newi,newj
    for i in range(0,len(magic_square)):
        for j in range(0,len(magic_square)):
            tk.Button(root,text=magic_square[i,j],width=15,bd=5).grid(row=i+2,column=j+2)
b1=tk.Button(root,text='click',width=15,command=matrix_generator)
b1.grid(row=1,column=1)
b2=tk.Button(root,text='Quit',width=15,command=root.destroy)
b2.grid(row=1,column=0)
root.mainloop()































































