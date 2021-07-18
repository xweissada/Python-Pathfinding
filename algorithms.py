from node import Node
from graph import Graph

def BFS ( graph, start ):
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
            if neighbor . state == 0:
                neighbor . ChangeState ( 1 )
                neighbor . depth = vertice . depth + 1
                queue . append ( neighbor )
        vertice . ChangeState ( 2 )
