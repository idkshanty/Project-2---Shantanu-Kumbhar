from node import Node

class Graph:
    def __init__(self):
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

    def getNodes(self):
        return self.nodes

    def getNode(self, nodeId):
        for node in self.nodes:
            if node.getId() == nodeId:
                return node
        return None

    def addEdge(self, sourceId, destId, action):
        source = self.getNode(sourceId)
        dest = self.getNode(destId)
        source.addConnection(dest, action)

    def bfs(self, startId):
        path = []
        visited = [startId]
        queue = [startId]
        while len(queue) > 0:
            currentId = queue.pop(0)   # take from the front
            path.append(currentId)
            current = self.getNode(currentId)
            if current.getIsGoal():
                return path
            for neighbor, action in current.getConnections():
                if neighbor.getId() not in visited:
                    visited.append(neighbor.getId())
                    queue.append(neighbor.getId())
        return []

    def dfs(self, startId):
        path = []
        visited = []
        stack = [startId]
        while len(stack) > 0:
            currentId = stack.pop()    # take from the back
            if currentId in visited:
                continue
            visited.append(currentId)
            path.append(currentId)
            current = self.getNode(currentId)
            if current.getIsGoal():
                return path
            for neighbor, action in current.getConnections():
                if neighbor.getId() not in visited:
                    stack.append(neighbor.getId())
        return []

    def __str__(self):
        return f"Graph with {len(self.nodes)} nodes"