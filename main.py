from node import Node
from graph import Graph
from algorithms import *

x = int ( input ( "Enter number of columns: " ) )
y = int ( input ( "Enter number of rows: " ) )

graph = Graph ( x, y )
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
