from random import randint
from BeyondClassicalSearch import BeyondClassicalSearch
class Node:
    def __init__(self, state):
        self.state = state
    def __gt__(self, other):
        return False

class GraphColoring:
    def __init__(self, numOfNode, numOfColor, graph):
        self.numOfNode = numOfNode
        self.numOfColor = numOfColor
        self.graph = graph
    
    def initialState(self):
        return Node([randint(0, self.numOfColor - 1) for i in range(numOfNode)])

    def neighbors(self, node):
        color = node.state
        neighbors = []
        for i in range(numOfNode):
            for j in range(numOfColor - 1):
                c = color.copy()
                c[i] = (c[i] + 1)%numOfColor
                neighbors.append(Node(c))
        return neighbors
    
    def randomNeighbor(self, node):
        color = node.state
        randomNode = randint(0, numOfNode - 1)
        randomColor = randint(0, numOfColor - 1)
        c = color.copy()
        c[randomNode] = randomColor
        return Node(c)
    
    def evaluate(self, node):
        if node == None:
            return float("-inf")
        color = node.state
        value = 0
        for i in range(numOfNode):
            for j in range(numOfNode):
                if self.graph[i][j] and color[i] == color[j]:
                    value -= 1
        return value

    def isGoal(self, node):
        if self.evaluate(node) == 0:
            return True
        else:
            False


numOfNode = int(input('number of node: '))
numOfColor = int(input('number fo color: '))
graph = [[False for i in range(numOfNode)] for j in range(numOfNode)]
for i in range(numOfNode):
    inp = input().split()
    for j in range(numOfNode):
        if inp[j] == '1':
            graph[i][j] = True


gc = GraphColoring(numOfNode, numOfColor, graph)
bc = BeyondClassicalSearch(gc)
print(bc.randomRestartHillClimbing().state)