import random
from BeyondClassicalSearch import BeyondClassicalSearch

class Node:
    def __init__(self, state):
        self.state = state
    def __gt__(self, other):
        return False

class Keyboard:
    def __init__(self):
        self.currentPopulation = []
        self.currentFitness = []
        self.maxFitnessValue = 0
        self.maxFitnessIndex = 0
        self.minFitnessValue = 14
        self.avrageFitnessValue = 0
    
    def randomPopulation(self):
        population = []
        for i in range(50):
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            left = []
            right = []
            for j in range(0, 13):
                rand = random.randint(0, len(letters) - 1)
                left.append(letters.pop(rand))
            for j in range(0, 13):
                rand = random.randint(0, len(letters) - 1)
                right.append(letters.pop(rand))
            population.append(Node([left, right]))
        return population

    def updateFitness(self, population):
        self.currentPopulation = population
        self.currentFitness = []
        self.maxFitnessValue = 0
        self.maxFitnessIndex = 0
        self.minFitnessValue = 14
        sumValue = 0
        for i in range(len(population)):
            value = self.evaluate(population[i])
            if self.maxFitnessValue < value:
                self.maxFitnessValue = value
                self.maxFitnessIndex = i
            if self.minFitnessValue > value:
                self.minFitnessValue = value
            sumValue += value
            for j in range(value):
                self.currentFitness.append(i)
        self.avrageFitnessValue = float(sumValue)/len(population)

    def randomSelection(self):
        return self.currentPopulation[self.currentFitness[random.randint(0, len(self.currentFitness) - 1)]]
    
    def produce(self, x, y):
        xLeft = x.state[0]
        xRight = x.state[1]
        yLeft = y.state[0]
        yRight = y.state[1]
        newLeft = []
        newRight = []
        temp = []
        for i in xLeft:
            if i in yLeft:
                newLeft.append(i)
            else:
                temp.append(i)
        for i in xRight:
            if i in yRight:
                newRight.append(i)
            else:
                temp.append(i)
        for i in range(len(temp)):
            if i%2 == 0:
                if len(newLeft) < 13:
                    newLeft.append(temp[i])
                else:
                    newRight.append(temp[i])
            else:
                if len(newRight) < 13:
                    newRight.append(temp[i])
                else:
                    newLeft.append(temp[i])
        return Node([newLeft, newRight])

    def mutate(self, node):
        left = node.state[0]
        right = node.state[1]
        randLeft = random.randint(0, 12)
        randRight = random.randint(0, 12)
        left[randLeft], right[randRight] = right[randRight], left[randLeft]
        return Node([left, right])

    def isGoal(self, node):
        if self.evaluate(node) == 13:
            return True
        return False

    def bestFitness(self):
        return self.currentPopulation[self.maxFitnessIndex]

    def evaluate(self, node):
        value = 1
        left = node.state[0]
        right = node.state[1]
        mainCharOnLeft = 0
        mainCharOnLeft += left.count('e')
        mainCharOnLeft += left.count('t')
        mainCharOnLeft += left.count('a')
        mainCharOnLeft += left.count('i')
        mainCharOnLeft += left.count('n')
        mainCharOnLeft += left.count('o')
        mainCharOnLeft += left.count('s')
        mainCharOnLeft += left.count('h')
        mainCharOnLeft += left.count('r')
        if mainCharOnLeft >= 5:
            mainCharOnLeft = 9 - mainCharOnLeft        
        value += mainCharOnLeft
        if left.count('t') + left.count('h') == 1:
            value += 1
        if left.count('e') + left.count('r') == 1:
            value += 1
        if left.count('o') + left.count('n') == 1:
            value += 1
        if left.count('a') + left.count('n') == 1:
            value += 1
        if left.count('r') + left.count('e') == 1:
            value += 1
        if left.count('h') + left.count('e') == 1:
            value += 1
        if left.count('i') + left.count('n') == 1:
            value += 1
        if left.count('e') + left.count('d') == 1:
            value += 1
        return value

k = Keyboard()
bc = BeyondClassicalSearch(k)
output = bc.geneticAlgorithms(k.randomPopulation())
print(output.state[0], output.state[1])