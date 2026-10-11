from node import Node
from graph import Graph

class World:
    graph = None

    def __init__(self, num):
        g = Graph()
        if num == 2:
            self.buildTwoCellWorld(g)
        self.setGraph(g)

    def buildTwoCellWorld(self, g):
        states = [(0, True, True),(0, True, False), (0, False, True),(0, False, False),(1, True, True),(1, True, False),(1, False, True),(1, False, False)]
        for i in range(len(states)):
            robot, dirtA, dirtB = states[i]
            isGoal = (not dirtA) and (not dirtB)
            g.addNode(Node(f"images/state_{i}.png", i, isGoal))
        for i in range(len(states)):
            robot, dirtA, dirtB = states[i]
            if robot == 1:
                g.addEdge(i, states.index((0, dirtA, dirtB)), "Move Left")
            if robot == 0:
                g.addEdge(i, states.index((1, dirtA, dirtB)), "Move Right")
            if robot == 0 and dirtA:
                g.addEdge(i, states.index((0, False, dirtB)), "Suck")
            if robot == 1 and dirtB:
                g.addEdge(i, states.index((1, dirtA, False)), "Suck")

    def getGraph(self):
        return self.graph

    def setGraph(self, gr):
        if type(gr) == Graph:
            print('successfully initialized')
            self.graph = gr