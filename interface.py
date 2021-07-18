from graph import Graph
from algorithms import *
from tkinter import *


class Interface:

    def __init__(self, x=10, y=10):
        self.graph = Graph(x, y)
        self.algorithm = 0
        self.window = Tk()
        self.window.title("Python Pathfinding")
        self.window.geometry("650x650")

        self.canvas = Canvas(self.window)

        self.drawCanvas()
        self.canvas.tag_bind("recClick", "<Button-1>", self.onClick)
        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.btn1 = Button(self.window, text="GO", width=10, command=self.buttonClick)
        self.btn1.place(x=150, y=510)
        self.btn2 = Button(self.window, text="Reset", width=10, command=self.drawCanvas)
        self.btn2.place(x=300, y=510)
        self.btn3 = Button(self.window, text="Change algorithm", width=10, command=self.changeAlgorithm)
        self.btn3.place(x=150, y=550)

    def drawCanvas(self):
        for node in self.graph.nodes:
            if node == self.graph.start:
                self.canvas.create_rectangle(node.x * 20, node.y * 20, (node.x + 1) * 20, (node.y + 1) * 20,
                                             fill="green",
                                             width=1)
            else:
                self.canvas.create_rectangle(node.x * 20, node.y * 20, (node.x + 1) * 20, (node.y + 1) * 20,
                                             fill=node.Color(), width=1, tags="recClick")

    def onClick(self, pos):
        node = int(pos.x / 20) + self.graph.y * (int(pos.y / 20))
        self.graph.nodes[node].ChangeWall()
        self.canvas.delete(ALL)
        self.drawCanvas()

    def buttonClick(self):
        if self.algorithm == 0:
                BFS(self.graph, self.graph.start, self.canvas, self.window)
        if self.algorithm == 1:
                DFS(self.graph, self.graph.start, self.canvas, self.window)

    def changeAlgorithm(self):
        self.algorithm += 1
        self.algorithm = self.algorithm % 2

    def Run(self):
        self.window.mainloop()
