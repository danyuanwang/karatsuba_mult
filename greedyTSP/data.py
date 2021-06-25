import math
from node import Node
class Data:
    def __init__(self):
        self.graph = []
        self.currentNode = None
        
    def getData(self, link):
        handle = open(link)
        for line in handle:
            a = line.split()
            print(a)
            node = Node(float(a[1]), float(a[2]), a[0])
            self.graph.append(node)

    def dist(self, a, b):
        dist = math.sqrt((a.x- b.x)**2 + (a.y- b.y)**2)
        return dist
    #takes a Data object of unexplored nodes explores the nearest one
    def explore(self, unexplored):
        #initializing 
        tempCurrentNode = self.currentNode
        least = unexplored.graph[0]
        #loop all unexplored nodes
        for node in unexplored.graph:
            #test if closest
            leastDist = self.dist(self.currentNode, least)
            nodeDist = self.dist(self.currentNode, node)
            if nodeDist < leastDist:
                least = node
            elif math.abs(nodeDist - leastDist) < 0.0000001:
                if(node.index < least.index):
                    least = node
        #explore the closest node
        self.addNode(least)
        unexplored.removeNode(least)

        return self.dist(tempCurrentNode, least)
            

    def addNode(self, node):
        self.graph.append(node)
        self.currentNode = node

    def removeNode(self, node):
        self.graph.remove(node)
