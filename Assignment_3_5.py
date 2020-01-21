import tkinter as tk
root=tk.Tk()
root.title("MAGIC SQUARE")
tk.Label(root,text="Enter the choice palyer1>").grid(row=0,column=0)
enter=tk.Entry(root)
enter.grid(row=0,column=1)
tk.Label(root,text="Enter the choice palyer2>").grid(row=1,column=0)
enter1=tk.Entry(root)
enter1.grid(row=1,column=1)
def compare(u1, u2):


    if u1 == u2:
        tk.Label(root,text="It's a tie!").grid(row=2,column=1)
    elif u1 == 'rock':
        if u2 == 'scissors':
            tk.Label(root,text="Rock wins!").grid(row=2,column=1)
        else:
            tk.Label(root,text="Paper wins!").grid(row=2,column=1)
    elif u1 == 'scissors':
        if u2 == 'paper':
            tk.Label(root,text="Scissors win!").grid(row=2,column=1)
        else:
            tk.Label(root,text="Rock wins!").grid(row=2,column=1)
    elif u1 == 'paper':
        if u2 == 'rock':
            tk.Label(root,text="Paper wins!").grid(row=2,column=1)
        else:
            tk.Label(root,text="Scissors win!").grid(row=2,column=1)
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")

def fun():
    global enter,enter1
    u1 = str(enter.get())
    u2 = str(enter1.get())
    print(u1,u2)
    compare(u1,u2)
    
b1=tk.Button(root,text='run',command=fun)
b1.grid(row=3,column=1)
root.mainloop()