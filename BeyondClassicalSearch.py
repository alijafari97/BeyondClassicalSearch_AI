import random
import math

class BeyondClassicalSearch:
    def __init__(self, problem):
        self.problem = problem

    def hillClimbing(self):
        node = self.problem.initialState()
        seenNodes = 0
        expandedNode = 0
        while True:
            neighbors = self.problem.neighbors(node)
            neighbor = max(neighbors, key=lambda node:self.problem.evaluate(node))
            seenNodes += len(neighbors)
            expandedNode += 1
            if self.problem.evaluate(neighbor) <= self.problem.evaluate(node):
                print('number of seen nodes: ', seenNodes)
                print('number of expanded nodes: ', expandedNode)
                return node
            print(node.state)
            node = neighbor

    def stochasticHillClimbing(self):
        node = self.problem.initialState()
        seenNodes = 0
        expandedNode = 0
        while True:
            goodNeighbors = []
            neighbors = self.problem.neighbors(node)
            (goodNeighbors.append(neighbor) for neighbor in neighbors if self.problem.evaluate(neighbor) > self.problem.evaluate(node))
            seenNodes += len(neighbors)
            expandedNode += 1
            if len(goodNeighbors) == 0:
                print('number of seen nodes: ', seenNodes)
                print('number of expanded nodes: ', expandedNode)
                return node
            node = random.choice(goodNeighbors)

    def firstChoiceHillClimbing(self):
        node = self.problem.initialState()
        maxCheck = 10
        seenNodes = 0
        expandedNode = 0
        while True:
            randomNeighbor = self.problem.randomNeighbor(node)
            seenNodes += 1
            for i in range(0, maxCheck):
                if self.problem.evaluate(randomNeighbor) <= self.problem.evaluate(node):
                    randomNeighbor = self.problem.randomNeighbor(node)
                    seenNodes += 1
                else:
                    break
            else:
                print('number of seen nodes: ', seenNodes)
                print('number of expanded nodes: ', expandedNode)
                return node
            node = randomNeighbor
            expandedNode += 1

    def randomRestartHillClimbing(self):
        bestNodeSeen = None
        seenNodes = 0
        expandedNode = 0
        for i in range(0, 20):
            node = self.problem.initialState()
            while True:
                neighbors = self.problem.neighbors(node)
                neighbor = max(neighbors, key=lambda node:self.problem.evaluate(node))
                seenNodes += len(neighbors)
                expandedNode += 1
                if self.problem.evaluate(neighbor) <= self.problem.evaluate(node):
                    if self.problem.isGoal(node):
                        print('number of seen nodes: ', seenNodes)
                        print('number of expanded nodes: ', expandedNode)
                        return node
                    else:
                        if self.problem.evaluate(node) > self.problem.evaluate(bestNodeSeen):
                            bestNodeSeen = node
                        break
                node = neighbor
        print('number of seen nodes: ', seenNodes)
        print('number of expanded nodes: ', expandedNode)
        return bestNodeSeen

    def simulatedAnnealing(self):
        currentNode = self.problem.initialState()
        t = 1
        seenNodes = 0
        expandedNode = 0
        while True:
            T = self.problem.schedule(t)
            if T < 0.01:
                print('number of seen nodes: ', seenNodes)
                print('number of expanded nodes: ', expandedNode)
                return currentNode
            nextNode = self.problem.randomNeighbor(currentNode)
            seenNodes += 1
            deltaE = self.problem.evaluate(nextNode) - self.problem.evaluate(currentNode)
            if deltaE > 0 :
                currentNode = nextNode
                expandedNode += 1
            elif random.random() < math.exp(float(deltaE)/T):
                currentNode = nextNode
                expandedNode += 1
            t += 1

    def geneticAlgorithms(self, population):
        newPopulation = []
        for t in range(10000):#maximum time
            self.problem.updateFitness(population)
            for i in range(len(population)):
                x = self.problem.randomSelection()
                y = self.problem.randomSelection()
                child = self.problem.produce(x, y)
                if random.random() < 0.1 :#probablity for mutation
                    child = self.problem.mutate(child)
                if self.problem.isGoal(child):
                    print(t, ' :')
                    return child
                newPopulation.append(child)
            population = newPopulation
            print(t, ' :')
            print('min value is: ', self.problem.minFitnessValue)
            print('max value is: ', self.problem.maxFitnessValue)
            print('avrage value is: ', self.problem.avrageFitnessValue)
        print(self.problem.maxFitnessValue)
        return self.problem.bestFitness()
