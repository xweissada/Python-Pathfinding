class Node:

    # Initialise the node with its coordinates, set the state to unknown and create an empty list with neighbors
    def __init__ ( self, x=0, y=0 ):
        self . x = x
        self . y = y
        self . state = 0
        self . neighbors = []

    # Return the Node as its coordinates
    def __repr__ ( self ):
        return "[" + str ( self . x ) + ":" + str ( self . y ) + "]"

    # Change the state of the Node to newState
    def ChangeState ( self, newState ):
        self . state = newState

    # Add a neighbor to the node
    def AddNeighbor ( self, x ):
        self . neighbors . append ( x )

    # Print all neighbors of the node
    def PrintNeighbors ( self ):
        for neighbor in self . neighbors:
            print ( neighbor, end = " " )
        print ()

    
test = Node ( 5, 7 )
print ( test )

print ( test . state )
test . ChangeState ( 5 )
print ( test . state )

test2 = Node ( 0, 0 )
test3 = Node ( 3, 5 )
test . AddNeighbor ( test2 )
test . AddNeighbor ( test3 )
test . PrintNeighbors ()
