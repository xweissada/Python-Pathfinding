import time


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
