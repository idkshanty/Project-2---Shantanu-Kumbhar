class Node:
    '''
    img: an image file (.png works) that shows the state
    id: the id for the state
    connections: a list of (otherNode, action) tuples reachable from this state
    isGoal: True if this state is a goal state (both cells clean)
    '''
    img = None
    id = -1
    connections = []
    isGoal = False

    def __init__(self, img=None, nodeId=-1, isGoal=False):
        self.img = img
        self.id = nodeId
        self.connections = []
        self.isGoal = isGoal

    def getImg(self):
        return self.img

    def getId(self):
        return self.id

    def getConnections(self):
        return self.connections

    def getIsGoal(self):
        return self.isGoal

    def setImg(self, img):
        self.img = img

    def setId(self, nodeId):
        self.id = nodeId

    def setIsGoal(self, isGoal):
        self.isGoal = isGoal

    def addConnection(self, otherNode, action):
        self.connections.append((otherNode, action))

    def __str__(self):
        return f"Node {self.id} (goal={self.isGoal})"