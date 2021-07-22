from graph import Graph
from algorithms import *
from tkinter import *


class Interface:

    def __init__(self, x=15, y=15):
        self.graph = Graph(x, y)
        self.window = Tk()
        self.window.title("Python Pathfinding")
        self.window.geometry("350x400")
        self.algorithm = StringVar(self.window)
        self.algorithm.set("BFS")

        self.canvas = Canvas(self.window)

        self.drawCanvas()
        self.canvas.tag_bind("recClick", "<Button-1>", self.onClick)
        self.canvas.pack(fill=BOTH, expand=True)

        self.btn1 = Button(self.window, text="GO", command=self.buttonClick)
        self.btn1.pack(side=RIGHT, pady=5, padx=5)
        self.btn2 = Button(self.window, text="Reset", command=self.drawCanvas)
        self.btn2.pack(side=RIGHT, pady=10, padx=5)
        self.drop = OptionMenu(self.window, self.algorithm, "BFS", "A*")
        self.drop.pack(side=RIGHT, pady=15, padx=5)

    def drawCanvas(self):
        for arr in self.graph.nodes:
            for node in arr:
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
        self.graph.nodes[int(pos.y / 20)][int(pos.x / 20)].ChangeWall()
        self.canvas.delete(ALL)
        self.drawCanvas()

    def buttonClick(self):
        if self.algorithm.get() == "BFS":
            BFS(self.graph, self.graph.start, self.graph.end, self.canvas, self.window)
        if self.algorithm.get() == "DFS":
            DFS(self.graph, self.graph.start, self.graph.end, self.canvas, self.window)
        if self.algorithm.get() == "A*":
            AStar(self.graph, self.graph.start, self.graph.end, self.canvas, self.window)

    def changeAlgorithm(self):
        self.algorithm += 1
        self.algorithm = self.algorithm % 2

    def Run(self):
        self.window.mainloop()
