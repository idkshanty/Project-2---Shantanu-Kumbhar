from node import Node
class Graph:
    '''
    nodes: the list of nodes, these should be node objects
    '''
    nodes = []
    
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
        ##BREADTHFIRSTSEARCH
        path = []
        visited = set()
        queue = [startId]
        visited.add(startId)

        while len(queue) > 0:
            currentId = queue.pop(0)
            path.append(currentId)
            currentNode = self.getNode(currentId)

            if currentNode.getIsGoal():
                return path

            for neighbor, action in currentNode.getConnections():
                if neighbor.getId() not in visited:
                    visited.add(neighbor.getId())
                    queue.append(neighbor.getId())

        return []

    def dfs(self, startId):
        ##DEPTHFIRST SEARCH
        path = []
        visited = set()
        stack = [startId]

        while len(stack) > 0:
            currentId = stack.pop()
            if currentId in visited:
                continue
            visited.add(currentId)
            path.append(currentId)
            currentNode = self.getNode(currentId)

            if currentNode.getIsGoal():
                return path

            for neighbor, action in currentNode.getConnections():
                if neighbor.getId() not in visited:
                    stack.append(neighbor.getId())

        return []

    def __str__(self):
        return f"Graph with {len(self.nodes)} nodes"