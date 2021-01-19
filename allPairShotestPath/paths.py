import sys
maxInt = 0xffffffff
def combineNode3(n1, n2, n3):
    return (((n1<<16) + n2) << 16) + n3
def combineNode(n1, n2):
    return (n1<<32) + n2
def decombineNodes(n):
    return [(n>>32)&0xffff, (n>>16)&0xffff,n&0xffff]
class Paths:
    def __init__(self):
        self.records = {}
        self.data = {}
        self.nodeCount = 1000
        handle = open('test.txt')
        firstline = True
        for line in handle:
            list = [int(v) for v in line.split()]
            if firstline:
                [self.nodeCount, self.edgeCount] = list
                firstline = False
            else:
                if list[0] in self.data:
                    self.data[list[0]].append(list[1])
                else:
                    self.data[list[0]] = [list[1]]
                self.records[combineNode3(list[0], list[1], 1)] = list[2]
                

    def NodeShortest(self):
        shortest = maxInt
        for source in range(len(self.data)):
            for i in range(self.nodeCount):
                for node in range(len(self.data)):
                    answer = self.getShortestDist(source, node, i)
                    self.records[source][node][i] = answer
                    if shortest > answer:
                        shortest = answer
        return shortest
    
    def getShortestDist(self, source, goal, i):
        if source == goal:
            return 0
        if i == 0:
            return maxInt

        choice1 = self.getShortestDist(source, goal, i-1)
        
        choice2 = maxInt
        nodeLinks = self.getNodeLinks(goal)
        nodeLinks.remove(source)
        for node in nodeLinks:
            temp0 = self.getShortestDist(goal, node, 1)
            if temp0 != maxInt:
                temp = self.getShortestDist(goal, node, i- 1) + temp0
            else:
                temp= maxInt
            if temp < choice2:
                temp = choice2
        return min(choice1, choice2)

    def getNodeLinks(self, goal):
        return self.data[goal]
