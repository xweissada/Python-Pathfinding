from graph import Graph
from algorithms import *
from tkinter import *

def drawCanvas ():
    for node in graph . nodes:
        if node == graph . start:
            canvas . create_rectangle ( node . x * 20, node . y * 20, ( node . x + 1 ) * 20, ( node . y + 1 ) * 20, fill = "green", width = 1 )
        else:
            canvas . create_rectangle ( node . x * 20, node . y * 20, ( node . x + 1 ) * 20, ( node . y + 1 ) * 20, fill = node . Color(), width = 1, tags = "recClick" )

def onClick ( pos ):
    node = int ( pos . x / 20 ) + y * ( int ( pos . y / 20 ) )
    graph . nodes[node] . ChangeWall()
    canvas . delete ( ALL )
    drawCanvas()

def buttonClick ():
    BFS ( graph, graph . start, canvas, window )

x = int ( input ( "Enter number of columns: " ) )
y = int ( input ( "Enter number of rows: " ) )

graph = Graph ( x, y )
graph . AddStart ( 44 )

window = Tk()
window . title ( "Python Pathfinding" )
window . geometry ( "650x650" )

canvas = Canvas ( window )

drawCanvas ()
canvas . tag_bind ( "recClick", "<Button-1>", onClick )
canvas . place ( relx = 0.5, rely = 0.5, anchor = CENTER )

btn = Button ( window, text = "GO", width = 10, command = buttonClick )
btn . place ( x = 250, y = 510 )

window . mainloop()

'''
print()
while ( True ):
    answ = int ( input ( "Enter 1 for BFS or 2 for DFS: " ) )
    if answ == 1:
        print( "BFS:" )
        BFS ( graph, graph . start )
    elif answ == 2:
        print( "DFS:" )
        DFS ( graph, graph . start )
    else:
        break
    print()
'''