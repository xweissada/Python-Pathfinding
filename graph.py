from node import Node

class Graph:

    def __init__ ( self, x = 3, y = 3 ):
        self . nodes = []
        for i in range ( y ):
            for j in range ( x ):
                self . nodes . append ( Node ( j, i ) )
                print ( self . nodes[-1], end = " " )
            print ()
        self . start = self . nodes[0]
        a = 0
        for node in self . nodes:
            if a % x > 0:
                node . AddNeighbor ( self . nodes[a-1] )
            if a - x >= 0:
                node . AddNeighbor ( self . nodes[a-x] )
            if a < ( x * y - 2 ) and a % x < x - 1:
                node . AddNeighbor ( self . nodes[a+1] )
            if a + x <= ( x * y - 1):
                node . AddNeighbor ( self . nodes[a+x] )
            a += 1
    def AddStart ( self, start ):
        self . start = self . nodes[start]
