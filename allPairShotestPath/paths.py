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
        self.parents = {}
        self.nodeCount = 1000
        handle = open('set2.txt')
        firstline = True
        for line in handle:
            list = [int(v) for v in line.split()]
            if firstline:
                [self.nodeCount, self.edgeCount] = list
                firstline = False
            else:
                if list[0] not in self.data:
                    self.data[list[0]] = []

                if list[0] not in self.parents:
                    self.parents[list[0]] = []

                if list[1] not in self.parents:
                     self.parents[list[1]] = []

                if list[1] not in self.data:
                    self.data[list[1]] = []
                self.data[list[0]].append(list[1])
                self.parents[list[1]].append(list[0])
                
                self.records[combineNode3(list[0], list[1], 1)] = list[2]

        print(self.records, self.data, self.parents)
                

    def NodeShortest(self):
        shortest = maxInt
        for source in range(1, len(self.data) + 1):
            print(source)
            for i in range(self.nodeCount):
                print("      ", i)
                for node in range(1, len(self.data) + 1):
                    print("           ", node)
                    answer = self.getShortestDist(source, node, i)
                    #print(source, node, i, answer)
                    self.records[combineNode3(source, node, i)] = answer
                    if shortest > answer and answer > 0:
                        shortest = answer
        return shortest
    
    def getShortestDist(self, source, goal, i):
        #print("new layer", i)
        if combineNode3(source, goal, i) in self.records:
            return self.records[combineNode3(source, goal, i)]

        if source == goal:
            #print("exit", i, 0)
            self.records[combineNode3(source, goal, i)] = 0
            return 0

        if i == 0:
            #print("exit", i, maxInt)
            self.records[combineNode3(source, goal, i)] = maxInt
            return maxInt

        if i == 1:
            if goal not in self.getNodeLinks(source):
                #print("exit", i, maxInt)
                self.records[combineNode3(source, goal, i)] = maxInt
                return maxInt


        choice1 = self.getShortestDist(source, goal, i-1)
        
        choice2 = maxInt
        nodeLinks = [] + self.getNodeParents(goal)
        if source in nodeLinks:
            nodeLinks.remove(source)
        for node in nodeLinks:
            temp0 = self.getShortestDist(goal, node, 1)
            temp = self.getShortestDist(goal, node, i- 1) + temp0
            if temp < choice2:
                temp = choice2
        #print("choices", choice1, choice2)
        solution = min(choice1, choice2)

        self.records[combineNode3(source, goal, i)] = solution
        #print("exit", i, solution)
        return solution

    def getNodeParents(self, goal):
        #print("goal", goal)
        return self.parents[goal]
    
    def getNodeLinks(self, goal):
        #print("goal children", goal)
        return self.data[goal]
