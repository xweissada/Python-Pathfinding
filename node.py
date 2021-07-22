class Node:

    # Initialise the node with its coordinates, set the state to unknown and create an empty neighbors list
    def __init__ ( self, x=0, y=0 ):
        self . x = x
        self . y = y
        self . f = 0
        self . h = 0
        self . g = 0
        self . state = 0
        self . wall = False
        self . depth = 0
        self . parent = None
        self . neighbors = []

    # Return the Node as its coordinates
    def __repr__ ( self ):
        return "[" + str ( self . x ) + ":" + str ( self . y ) + "]"
    
    def __lt__ ( self, other ):
        return self.f < other.f

    # Change the state of the Node to newState ( 0 .. unknown, 1 .. opened, 2 .. closed )
    def ChangeState ( self, newState ):
        self . state = newState

    def ChangeWall ( self ):
        if self . wall:
            self . wall = False
        else:
            self . wall = True

    def Color ( self ):
        if self . wall:
            return "black"
        else:
            return "white"

    # Add a neighbor to the node
    def AddNeighbor ( self, x ):
        self . neighbors . append ( x )

    # Print all neighbors of the node
    def PrintNeighbors ( self ):
        for neighbor in self . neighbors:
            print ( neighbor, end = " " )
        print ()
