from BeyondClassicalSearch import BeyondClassicalSearch
from random import randint
import copy

class Node:
    def __init__(self, state):
        self.state = state
    def __gt__(self, other):
        return False

class LettersTable:
    def __init__(self, n, m, table, sizeOfDictionary, dictionary):
        self.n = n
        self.m = m
        self.table = table
        self.sizeOfDictionary =sizeOfDictionary
        self.dictionary =dictionary
        self.initialNode = Node(table)
        self._val = 0
        self._lastAction = ''
    
    def initialState(self):
        return self.initialNode

    def randomNeighbor(self, node):
        table = copy.deepcopy(node.state)
        i1 = randint(0, self.n - 1)
        j1 = randint(0, self.m - 1)
        i2 = randint(0, self.n - 1)
        j2 = randint(0, self.m - 1)
        table[i1][j1], table[i2][j2] =  table[i2][j2] ,table[i1][j1]
        return Node(table)

    def evaluate(self, node):
        table = node.state
        self._val = 0
        for i in range(self.sizeOfDictionary):
            word = self.dictionary[i]
            for n in range(self.n):
                for m in range(self.m):
                    if word[0] == table[n][m]:
                        self._value(table, n, m, word[1:])
        return self._val
        
    
    def _value(self, table, n, m, word):
        if word == '':
            self._val += 10
            return None
        if(n > 0 and self._lastAction != 'D') and word[0] == table[n-1][m]:
            self._val += 1
            self._lastAction = 'U'
            self._value(table, n-1, m, word[1:])
        if(n < self.n - 1 and self._lastAction != 'U') and word[0] == table[n+1][m]:
            self._val += 1
            self._lastAction = 'D'
            self._value(table, n+1, m, word[1:])
        if(m > 0 and self._lastAction != 'R') and word[0] == table[n][m-1]:
            self._val += 1
            self._lastAction = 'L'
            self._value(table, n, m-1, word[1:])
        if(m < self.m - 1 and self._lastAction != 'L') and word[0] == table[n][m+1]:
            self._val += 1
            self._lastAction = 'R'
            self._value(table, n, m+1, word[1:])
        return None

    def schedule(self, t):
        return (((10000000-t)/10000000)*1.5)**9



inp = input()

split = inp.split()
n = int(split[0])
m = int(split[1])

table = []
for i in range(n):
    inp = input().split()
    table.append(inp)

sizeOfDictionary = int(input())
dictionary = []
for i in range(sizeOfDictionary):
    dictionary.append(input())

lt = LettersTable(n, m, table, sizeOfDictionary, dictionary)
bc = BeyondClassicalSearch(lt)

temp=bc.simulatedAnnealing().state
[print(x) for x in temp]