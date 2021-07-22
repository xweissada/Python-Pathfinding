import time
import bisect


def BFS(graph, start, end, canvas, window):
    for arr in graph.nodes:
        for node in arr:
            node.ChangeState(0)
            node.depth = 0
            node.parent = None
    queue = []
    queue.append(start)
    start.ChangeState(1)
    while queue:
        vertice = queue.pop(0)
        print(str(vertice.depth) + " " + str(vertice))
        for neighbor in vertice.neighbors:
            if neighbor.state == 0 and not neighbor.wall:
                if neighbor == end:
                    end.parent = vertice
                    queue.clear()
                    break
                neighbor.ChangeState(1)
                canvas.create_rectangle(neighbor.x * 20, neighbor.y * 20, (neighbor.x + 1) * 20, (neighbor.y + 1) * 20,
                                        fill="yellow", width=1)
                window.update()
                time.sleep(0.1)
                neighbor.depth = vertice.depth + 1
                neighbor.parent = vertice
                queue.append(neighbor)
        vertice.ChangeState(2)
        if vertice != graph.start:
            canvas.create_rectangle(vertice.x * 20, vertice.y * 20, (vertice.x + 1) * 20, (vertice.y + 1) * 20,
                                    fill="blue", width=1)
        window.update()
        time.sleep(0.1)
    path = end.parent
    while path.parent != None:
        canvas.create_rectangle(path.x * 20, path.y * 20, (path.x + 1) * 20, (path.y + 1) * 20,
                                    fill="purple", width=1)
        path = path.parent
        


def DFSRec(node, start, end, canvas, window):
    if node.state == 1 or node.state == 2 or node.wall:
        return
    print(node)
    node.state = 1
    if node != start:
        canvas.create_rectangle(node.x * 20, node.y * 20, (node.x + 1) * 20, (node.y + 1) * 20, fill="yellow", width=1)
    window.update()
    time.sleep(0.1)
    for neighbor in node.neighbors:
        DFSRec(neighbor, start, end, canvas, window)
    node.state = 2
    if node != start:
        canvas.create_rectangle(node.x * 20, node.y * 20, (node.x + 1) * 20, (node.y + 1) * 20, fill="blue", width=1)
    window.update()
    time.sleep(0.1)


def DFS(graph, start, end, canvas, window):
    for arr in graph.nodes:
        for node in arr:
            node.ChangeState(0)
            node.depth = 0
    DFSRec(start, start, end, canvas, window)


def GetHeuristic (node, end):
    return abs(node.x - end.x) + abs(node.y - end.y)

def AStar(graph, start, end, canvas, window):
    for arr in graph.nodes:
        for node in arr:
            node.ChangeState(0)
            node.f=0
            node.g=0
            node.h=0
            node.parent=None
    openNodes = []
    closedNodes = []
    openNodes.append(start)
    while openNodes:
        currentNode = openNodes.pop(0)
        closedNodes.append(currentNode)
        if currentNode != start:
            canvas.create_rectangle(currentNode.x * 20, currentNode.y * 20, (currentNode.x + 1) * 20, (currentNode.y + 1) * 20, fill="blue", width=1)
        for node in currentNode.neighbors:
            print(node)
            if node == end:
                end.parent = currentNode
                openNodes.clear()
                break
            if node not in closedNodes and not node.wall:
                gValue = currentNode.g + 10
                hValue = GetHeuristic(node, end)
                fValue = node.g + node.h
                if node in openNodes and node.f < fValue:
                    openNodes.remove(node)
                    node.parent = currentNode
                    node.g = gValue
                    node.h = hValue
                    node.f = fValue
                    bisect.insort(openNodes, node)
                else:
                    node.parent = currentNode
                    node.g = gValue
                    node.h = hValue
                    node.f = fValue
                    bisect.insort(openNodes, node)
                    canvas.create_rectangle(node.x * 20, node.y * 20, (node.x + 1) * 20, (node.y + 1) * 20, fill="yellow", width=1)
                    window.update()
                    time.sleep(0.1)
    path = end.parent
    while path.parent != None:
        canvas.create_rectangle(path.x * 20, path.y * 20, (path.x + 1) * 20, (path.y + 1) * 20,
                                    fill="purple", width=1)
        path = path.parent