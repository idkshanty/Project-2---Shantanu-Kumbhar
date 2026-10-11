from node import Node
from graph import Graph


class World:

    graph = None
    def __init__(self, num):
        #num is how many cells
        g = Graph()

        if num == 2:
            self.buildTwoCellWorld(g)
        elif num == 3:
            self.buildThreeCellWorld(g)

        self.setGraph(g)

    def buildTwoCellWorld(self, g):
        # state = (robotLocation, dirtA, dirtB)
        # robotLocation: 0 = cell A, 1 = cell B
        # dirtA/dirtB: True = dirty, False = clean
        states = [
            (0, True, True),    # 0
            (0, True, False),   # 1
            (0, False, True),   # 2
            (0, False, False),  # 3  GOAL
            (1, True, True),    # 4
            (1, True, False),   # 5
            (1, False, True),   # 6
            (1, False, False),  # 7  GOAL
        ]

        for nodeId, state in enumerate(states):
            robot, dirtA, dirtB = state
            isGoal = (not dirtA) and (not dirtB)
            imgPath = f"images/state_{nodeId}.png"
            g.addNode(Node(img=imgPath, nodeId=nodeId, isGoal=isGoal))

        for nodeId, state in enumerate(states):
            robot, dirtA, dirtB = state

            # Move Left: only has an effect if robot is in cell B
            if robot == 1:
                destState = (0, dirtA, dirtB)
                destId = states.index(destState)
                g.addEdge(nodeId, destId, "Move Left")

            # Move Right: only has an effect if robot is in cell A
            if robot == 0:
                destState = (1, dirtA, dirtB)
                destId = states.index(destState)
                g.addEdge(nodeId, destId, "Move Right")

            # Suck: cleans whichever cell the robot is in
            if robot == 0 and dirtA:
                destState = (0, False, dirtB)
                destId = states.index(destState)
                g.addEdge(nodeId, destId, "Suck")
            if robot == 1 and dirtB:
                destState = (1, dirtA, False)
                destId = states.index(destState)
                g.addEdge(nodeId, destId, "Suck")

    def buildThreeCellWorld(self, g):
        # state = (robotLocation, dirtA, dirtB, dirtC)
        # robotLocation: 0 = cell A, 1 = cell B, 2 = cell C
        states = []
        for robot in range(3):
            for dirtA in (True, False):
                for dirtB in (True, False):
                    for dirtC in (True, False):
                        states.append((robot, dirtA, dirtB, dirtC))

        for nodeId, state in enumerate(states):
            robot, dirtA, dirtB, dirtC = state
            isGoal = (not dirtA) and (not dirtB) and (not dirtC)
            imgPath = f"images/state3_{nodeId}.png"
            g.addNode(Node(img=imgPath, nodeId=nodeId, isGoal=isGoal))

        for nodeId, state in enumerate(states):
            robot, dirtA, dirtB, dirtC = state
            dirt = [dirtA, dirtB, dirtC]

            if robot > 0:
                destDirt = dirt[:]
                destState = (robot - 1, *destDirt)
                g.addEdge(nodeId, states.index(destState), "Move Left")

            if robot < 2:
                destDirt = dirt[:]
                destState = (robot + 1, *destDirt)
                g.addEdge(nodeId, states.index(destState), "Move Right")

            if dirt[robot]:
                destDirt = dirt[:]
                destDirt[robot] = False
                destState = (robot, *destDirt)
                g.addEdge(nodeId, states.index(destState), "Suck")


    def getGraph(self):
        return self.graph

    def setGraph(self, gr):
        if type(gr) == Graph:
            print('successfully initialized')
            self.graph = gr