from node import Node
from graph import Graph
from tkinter import *
import time

def BFS ( graph, start, canvas, window ):
    for node in graph . nodes:
        node . ChangeState ( 0 )
        node . depth = 0
    queue = []
    queue . append ( start )
    start . ChangeState ( 1 )
    while queue:
        vertice = queue . pop(0)
        print ( str ( vertice . depth ) + " " + str ( vertice ) )
        for neighbor in vertice . neighbors:
            if neighbor . state == 0 and not neighbor . wall:
                neighbor . ChangeState ( 1 )
                canvas . create_rectangle ( neighbor . x * 20, neighbor . y * 20, ( neighbor . x + 1 ) * 20, ( neighbor . y + 1 ) * 20, fill = "yellow", width = 1 )
                window . update()
                time . sleep ( 0.1 )
                neighbor . depth = vertice . depth + 1
                queue . append ( neighbor )
        vertice . ChangeState ( 2 )
        if vertice != graph . start:
            canvas . create_rectangle ( vertice . x * 20, vertice . y * 20, ( vertice . x + 1 ) * 20, ( vertice . y + 1 ) * 20, fill = "blue", width = 1 )
        window . update()
        time . sleep ( 0.1 )

def DFSRec ( node ):
    if node . state == 1 or node . state == 2:
        return
    print ( node )
    node . state = 1
    for neighbor in node . neighbors:
        DFSRec ( neighbor )
    node . state = 2 

def DFS ( graph, start ):
    for node in graph . nodes:
        node . ChangeState ( 0 )
        node . depth = 0
    DFSRec ( start )