class Node:
    def __init__(self, img=None, nodeId=-1, isGoal=False):
        self.img = img
        self.id = nodeId
        self.isGoal = isGoal
        self.connections = []

    def getImg(self):
        return self.img

    def getId(self):
        return self.id

    def getIsGoal(self):
        return self.isGoal

    def getConnections(self):
        return self.connections

    def setImg(self, img):
        self.img = img

    def setId(self, nodeId):
        self.id = nodeId

    def addConnection(self, otherNode, action):
        self.connections.append((otherNode, action))

    def __str__(self):
        return f"Node {self.id} (goal={self.isGoal})"