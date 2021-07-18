from node import Node


class Graph:

    # Creates all the nodes in the grid and adds the respective neighbors for every node
    def __init__(self, x=3, y=3):
        self.x = x
        self.y = y
        self.nodes = []
        for i in range(y):
            for j in range(x):
                self.nodes.append(Node(j, i))

        self.start = self.nodes[0]
        a = 0
        for node in self.nodes:
            if a % x > 0:
                node.AddNeighbor(self.nodes[a - 1])
            if a - x >= 0:
                node.AddNeighbor(self.nodes[a - x])
            if a < (x * y - 1) and a % x < x - 1:
                node.AddNeighbor(self.nodes[a + 1])
            if a + x <= (x * y - 1):
                node.AddNeighbor(self.nodes[a + x])
            a += 1

    # Changes the starting point of the graph
    def AddStart(self, node):
        self.start = self.nodes[node]
