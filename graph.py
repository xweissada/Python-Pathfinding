class Graph:

    def __init__ ( self ):
        self . nodes = []

    def AddNode ( self, node ):
        self . nodes . append ( node )

    def AddStart ( self, node ):
        self . start = node
        self . AddNode ( node )
