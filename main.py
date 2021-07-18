from node import Node
from graph import Graph
from algorithms import BFS

n1 = Node ( 0, 0 )
n2 = Node ( 0, 1 )
n3 = Node ( 1, 0 )
n4 = Node ( 1, 1 )
n5 = Node ( 4, 6 )
n1 . AddNeighbor ( n2 )
n1 . AddNeighbor ( n3 )
n3 . AddNeighbor ( n4 )
n2 . AddNeighbor ( n5 )
n3 . AddNeighbor ( n5 )
graph = Graph()
graph . AddStart ( n1 )
graph . AddNode ( n2 )
graph . AddNode ( n3 )
graph . AddNode ( n4 )
graph . AddNode ( n5 )
BFS ( graph, graph . start )