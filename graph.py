from node import Node


class Graph:

    # Creates all the nodes in the grid and adds the respective neighbors for every node
    def __init__(self, x=3, y=3):
        self.x = x
        self.y = y
        self.nodes = []
        for i in range(y):
            new = []
            for j in range(x):
                new.append(Node(j, i))
            self.nodes.append(new)

        self.start = self.nodes[0][0]
        self.end = self.nodes[-1][-1]
        i = 0
        j = 0
        for a in self.nodes:
            for b in a:
                if j < y - 1:
                    b.AddNeighbor(self.nodes[i][j+1])
                if j < y - 1 and i < x - 1:
                    b.AddNeighbor(self.nodes[i+1][j+1])
                if i < x - 1:
                    b.AddNeighbor(self.nodes[i+1][j])
                if i < x - 1 and j > 0:
                    b.AddNeighbor(self.nodes[i+1][j-1])
                if j > 0:
                    b.AddNeighbor(self.nodes[i][j-1])
                if i > 0 and j > 0:
                    b.AddNeighbor(self.nodes[i-1][j-1])
                if i > 0:
                    b.AddNeighbor(self.nodes[i-1][j])
                if i > 0 and j < y - 1:
                    b.AddNeighbor(self.nodes[i-1][j+1])
                j += 1
            i += 1
            j = 0

    # Changes the starting point of the graph
    def AddStart(self, node):
        self.start = self.nodes[node]
