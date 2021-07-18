from graph import Graph
from algorithms import *
from tkinter import *


class Interface:

    def __init__(self, x=10, y=10):
        self.graph = Graph(x, y)
        self.graph.AddStart(45)
        self.window = Tk()
        self.window.title("Python Pathfinding")
        self.window.geometry("650x650")
        self.algorithm = StringVar(self.window)
        self.algorithm.set("BFS")

        self.canvas = Canvas(self.window)

        self.drawCanvas()
        self.canvas.tag_bind("recClick", "<Button-1>", self.onClick)
        self.canvas.pack()

        self.btn1 = Button(self.window, text="GO", command=self.buttonClick)
        self.btn1.pack()
        self.btn2 = Button(self.window, text="Reset", command=self.drawCanvas)
        self.btn2.pack()
        self.drop = OptionMenu(self.window, self.algorithm, "BFS", "DFS")
        self.drop.pack()

    def drawCanvas(self):
        for node in self.graph.nodes:
            if node == self.graph.start:
                self.canvas.create_rectangle(node.x * 20, node.y * 20, (node.x + 1) * 20, (node.y + 1) * 20,
                                             fill="green", width=1)
            elif node == self.graph.end:
                self.canvas.create_rectangle(node.x * 20, node.y * 20, (node.x + 1) * 20, (node.y + 1) * 20,
                                             fill="red", width=1)
            else:
                self.canvas.create_rectangle(node.x * 20, node.y * 20, (node.x + 1) * 20, (node.y + 1) * 20,
                                             fill=node.Color(), width=1, tags="recClick")

    def onClick(self, pos):
        node = int(pos.x / 20) + self.graph.y * (int(pos.y / 20))
        self.graph.nodes[node].ChangeWall()
        self.canvas.delete(ALL)
        self.drawCanvas()

    def buttonClick(self):
        if self.algorithm.get() == "BFS":
                BFS(self.graph, self.graph.start, self.graph.end, self.canvas, self.window)
        if self.algorithm.get() == "DFS":
                DFS(self.graph, self.graph.start, self.graph.end, self.canvas, self.window)

    def changeAlgorithm(self):
        self.algorithm += 1
        self.algorithm = self.algorithm % 2

    def Run(self):
        self.window.mainloop()
