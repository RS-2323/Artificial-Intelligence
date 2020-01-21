#create button with print functon onclick
import tkinter
window=tkinter.Tk()
window.title("GUI")
def PrintOnClick():
    tkinter.Label(window,text="Welcome!").pack()
tkinter.Button(window,text="Click me!",command=PrintOnClick).pack()
window.mainloop()
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------



#print image
import tkinter
window=tkinter.Tk()
window.title("GUI")
icon=tkinter.PhotoImage(file="skeleton.png")
label=tkinter.Label(window,image=icon).pack()
window.mainloop()
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------



#stark
stark=['ria','sapna','dushyant']
stark.append('ayush')
stark.append('aarzoo')
print(stark)
print(stark.pop())
print(stark)
print(stark.pop())
print(stark)
print(stark.pop())
print(stark)
print(stark.pop())
print(stark)
print(stark.pop())
print(stark)
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------


#deque
import collections 
from collections import deque
qwerty=deque(['ria','sapna','dushyant'])
print(qwerty)
qwerty.append('arzoo')
print(qwerty)
qwerty.append('ritu')
print(qwerty)
print(qwerty.popleft())
print(qwerty)
#---
de = collections.deque([1,2,3]) 
de.append(4) 
print ("The deque after appending at right is : ") 
print (de) 
de.appendleft(6) 
print ("The deque after appending at left is : ") 
print (de)  
de.pop() 
print ("The deque after deleting from right is : ") 
print (de) 
de.popleft() 
print ("The deque after deleting from left is : ") 
print (de)
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------

#queue
import queue   
L = queue.Queue(maxsize=20)  
L.put(5) 
L.put(9) 
L.put(1) 
L.put(7) 
print(L.get()) 
print(L.get()) 
print(L.get()) 
print(L.get()) 
#-----------
import collections 
de = collections.deque([1,2,3]) 
de.append(4) 
print ("The deque after appending at right is : ") 
print (de) 
de.appendleft(6) 
print ("The deque after appending at left is : ") 
print (de)  
de.pop() 
print ("The deque after deleting from right is : ") 
print (de) 
de.popleft() 
print ("The deque after deleting from left is : ") 
print (de)
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------



#create node tree
from treelib import Node,Tree
new_Tree=Tree()
new_Tree.create_node("n1",1)
new_Tree.create_node("n2",2,parent=1)
new_Tree.create_node("n3",3,parent=1)
new_Tree.create_node("n4",4,parent=3)
new_Tree.create_node("n5",5,parent=4)
new_Tree.show()
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#calculator
import tkinter as tk
from functools import partial
def call_result(label_result,n1,n2):
    num1=(n1.get())
    num2=(n1.get())
    result=int(num1)+int(num2)
    label_result.config(text="Result is %d" % result)
    return
root=tk.Tk()
root.geometry('400x200+100+200')
root.title('Calculator-Addition')

number1=tk.StringVar()
number2=tk.StringVar()

labelTitle=tk.Label(root,text="Calculator=Addition").grid(row=0,column=2)
labelNum1=tk.Label(root,text="Enter a number").grid(row=1,column=0)
labelNum2=tk.Label(root,text="Enter another number").grid(row=2,column=0)

labelResult=tk.Label(root)
labelResult.grid(row=7,column=2)

entryNum1=tk.Entry(root,textvariable=number1).grid(row=1,column=2)
entryNum2=tk.Entry(root,textvariable=number2).grid(row=2,column=2)

call_result=partial(call_result,labelResult,number1,number2)
buttonCal=tk.Button(root,text="Calculate",command=call_result).grid(row=3,column=2)
root.mainloop()




#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------#---------------------------------------------------------------------------------------------------------



#sqlite3 database
import sqlite3
connection=sqlite3.connect("mytable.db")
crsr=connection.cursor()

sql_command="""CREATE TABLE emp(
Staff_number INTEGER PRIMARY KEY,
fname VARCHAR(20),
lname VARCHAR(30),
gender CHAR(1),
joining DATE);"""
sql_command="""INSERT INTO emp VALUES(77,"ria", "sharma","F","2019-09-17");"""
crsr.execute(sql_command)

sql_command="""INSERT INTO emp VALUES(23,"ayush", "soni","F","2019-09-12");"""
crsr.execute(sql_command)

connection.commit()
connection.close()
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------



#series
a = int(input("Enter A positive number:"))
b = int(input("Enter A positive number:"))
if a<0 or b<0:
    print("Enter a valid number")
else:
    print(a)
    print(b)
    def fun(a,b):
        for i in range(0,7):
            c = a+b
            print(c)
            a=b
            b=c
        fun(a,b)
    
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------



#linear search
list1 = [1,2,3,4,5,6,7,8,9,0]

number = int(input("Enter a number to cheak:"))
if number in list1:
    print(number)
else:
    print("Does not exist")
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------


#google search
from googlesearch import googlesearch

query = "bhartiya skill development univercity jaipur"

for j in googlesearch(query,tld="co.in"):
    print(j)
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------



#OOP-Class-and-BFS Python ImplementationPage
class demo(object):

    def __init__(self, a):

        self.a = a
        
    def change_a(self, new_a):

        self.a = new_a

obj1 = demo(10)      

print(obj1.a)         


obj1.change_a(20)    

print(obj1.a)       

#Class Ex-2

class car(): 

    def __init__(self, model, color): 

        self.model = model 

        self.color = color 

    def show(self): 

        print("Model is", self.model ) 

        print("color is", self.color ) 

tata = car("TATA Safari Storme", "White") 
fortuner = car("Fortuner MT 2694 ", "RED") 
tata.show()	 
fortuner.show() 
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------



#BFS implementation on Tree in Python

"""

        1

        /  \

       2    3

      / \     / \

     4   5  6  7

    """

class TNode:

  def __init__(self, data, left=None, right=None):

    self.data = data

    self.left = left

    self.right = right



class BST:

  def __init__(self, root):

    self._root = root



  def bfs(self):

    list = [self._root]

    while len(list) > 0:

        print([e.data for e in list])

        list = [e.left for e in list if e.left] + [e.right for e in list if e.right]

bst = BST(TNode(1, TNode(2, TNode(4), TNode(5)), TNode(3, TNode(6), TNode(7))))

bst.bfs()
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------


#DFS implementation on Tree in Python
"""

          A

        /   \    \

      B    C    D

            /       /

           F      E



"""

class Tree(object):

    def __init__(self, name='root', children=None):

        self.name = name

        self.children = []

        if children is not None:

            for child in children:

                self.add_child(child)

    def __repr__(self):

        return self.name

    def add_child(self, node):

        assert isinstance(node, Tree)

        self.children.append(node)

tree = Tree('A', [Tree('B'),

                      Tree('C', [Tree('F')]),

                      Tree('D', [Tree('E')])])

def DFS(tree, node):

    print(tree)

    if tree.name == node:

        print(f'found node: {node} in {tree}')

        return tree

    for child in tree.children:

        print(child)

        if child.name == node:

            print(f'found node: {node} in {child}')

            return child

        if child.children:

            print(f'attempt searching {child} for {node}')

            match = DFS(child, node)

            if match:

                print(match)

                return match

result = DFS(tree, 'E')

print("Result:",result)



#=========================

#DFS with Stack and Adjacency Metrix

#------------------------------------

def dfs_iterative(graph, start):

    stack, path = [start], []

    while stack:

        vertex = stack.pop()

        if vertex in path:

            continue

        path.append(vertex)

        for neighbor in graph[vertex]:

            stack.append(neighbor)

    return path

adjacency_matrix = {1: [2, 3], 2: [4, 5],

                    3: [5], 4: [6], 5: [6],

                    6: [7], 7: []}
print(dfs_iterative(adjacency_matrix, 1))
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------


#shortest path

G=nx.path_graph(5)
print(nx.shortest_path(G,source=0,target=4))
p=nx.shortest_path(G,source=0) # target not specified
p[4]
p=nx.shortest_path(G,target=4) # source not specified
p[0]
p=nx.shortest_path(G) # source,target not specified
p[0][4]


#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------




#Python Programs Magic Square and Tic-Tac-Toe GamePage
# Create an N x N magic square. N must be odd.

import numpy as np
N  = int(input("Enter the value of N for NxN matrix:"))
magic_square = np.zeros((N,N), dtype=int)
n = 1
i, j = 0, N//2
while n <= N**2:

    magic_square[i, j] = n

    n += 1

    newi, newj = (i-1) % N, (j+1)% N

    if magic_square[newi, newj]:

        i += 1

    else:

        i, j = newi, newj
print(magic_square)

#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------



#Full Game -Tic Tac Toe-Two User 

from tkinter import *

import tkinter.messagebox

click = True

tk = None

def start():

    global tk

    tk = Tk()

    tk.title("Game-Tic Tac Toe:Two Player")



    def play(button):

        global click, tk



        if button["text"] == " " and click:

            button["text"] = "X"

            click = False

        elif button["text"] == " ":

            button['text'] = "O"

            click = True



        if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or

            button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or

            button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or

            button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or

            button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or

            button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or

            button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or

            button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):

            answer = tkinter.messagebox.askquestion('X Player wins!!!', 'Do you want to play again')

            tk.destroy()

            if answer == 'yes': start()



        elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or

            button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or

            button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or

            button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or

            button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or

            button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or

            button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or

            button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):

            answer = tkinter.messagebox.askquestion('O Player wins!!!', 'Do you want to play again')

            tk.destroy()

            if answer == 'yes': start()



    button1 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button1))

    button1.grid(row=1, column=0)



    button2 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button2))

    button2.grid(row=1, column=1)



    button3 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button3))

    button3.grid(row=1, column=2)



    button4 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button4))

    button4.grid(row=2, column=0)



    button5 = Button(tk, text=" ", font=("Times 26 bold"), height=4, width=8, command=lambda:play(button5))

    button5.grid(row=2, column=1)



    button6 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button6))

    button6.grid(row=2, column=2)



    button7 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button7))

    button7.grid(row=3, column=0)



    button8 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button8))

    button8.grid(row=3, column=1)



    button9 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button9))

    button9.grid(row=3, column=2)
    tk.mainloop()
start()

#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------



#Tower of Hanoi(TOH) Problem in Python
def hanoi(ndisks, startPeg=1, endPeg=3):

    if ndisks:

        hanoi(ndisks-1, startPeg, 6-startPeg-endPeg)

        print("Move disk %d from peg %d to peg %d" % (ndisks, startPeg, endPeg))

        hanoi(ndisks-1, 6-startPeg-endPeg, endPeg)

hanoi(ndisks=3)
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
 
 
 
#Water Jug Problem in Python
def pour(jug1, jug2):

    max1, max2, fill = 5,7,4 #Change maximum capacity and final capacity

    print("%d\t%d" % (jug1, jug2))

    if jug2 is fill:

        return

    elif jug2 is max2:

        pour(0, jug1)

    elif jug1 != 0 and jug2 is 0:

        pour(0, jug1)

    elif jug1 is fill:

        pour(jug1, 0)

    elif jug1 < max1:

        pour(max1, jug2)

    elif jug1 < (max2-jug2):

        pour(0, (jug1+jug2))

    else:
        pour(jug1-(max2-jug2), (max2-jug2)+jug2)
print("JUG1\tJUG2")
pour(0, 0)

#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------













#TSP Problem in Python
import mlrose
dist_list = [(0, 1, 3.1623), (0, 2, 4.1231), (0, 3, 5.8310), (0, 4, 4.2426), (0, 5, 5.3852), \

             (0, 6, 4.0000), (0, 7, 2.2361), (1, 2, 1.0000), (1, 3, 2.8284), (1, 4, 2.0000), \

             (1, 5, 4.1231), (1, 6, 4.2426), (1, 7, 2.2361), (2, 3, 2.2361), (2, 4, 2.2361), \

             (2, 5, 4.4721), (2, 6, 5.0000), (2, 7, 3.1623), (3, 4, 2.0000), (3, 5, 3.6056), \

             (3, 6, 5.0990), (3, 7, 4.1231), (4, 5, 2.2361), (4, 6, 3.1623), (4, 7, 2.2361), \

             (5, 6, 2.2361), (5, 7, 3.1623), (6, 7, 2.2361)]
fitness_dists = mlrose.TravellingSales(distances = dist_list)
problem_fit2 = mlrose.TSPOpt(length = 8, fitness_fn = fitness_dists, maximize = False)
best_state, best_fitness = mlrose.genetic_alg(problem_fit2, mutation_prob = 0.2, max_attempts = 100,random_state = 2)
print(best_fitness)
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
