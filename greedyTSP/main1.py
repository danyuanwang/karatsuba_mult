import math
import sys
from node import Node
class Data:
    def __init__(self):
        self.graph = []
        
    def dist(self, a, b):
        dist = math.sqrt((float(a[1])- float(b[1]))**2 + (float(a[2])- float(b[2]))**2)
        return dist
    #takes a Data object of unexplored nodes explores the nearest one
    def explore(self, link):
        #initializing 
        
        handle = open(link)
        for line in handle:
            a = line.split()
            print(a)
            #node = Node(float(a[1]), float(a[2]), a[0])
            self.graph.append(a)

        current = self.graph.pop(0)
        first = current
        leastDist = sys.float_info.max 
        least = None
        total = 0.0
        while(len(self.graph) > 0):
            #loop all unexplored nodes
            for node in self.graph:
                #test if closest
                nodeDist = self.dist(current, node)
                if nodeDist < leastDist:
                    least = node
                    leastDist = nodeDist
                elif abs(nodeDist - leastDist) < 0.0000001:
                    if(int(node[0]) < int(least[0])):
                        least = node
                        leastDist = nodeDist

            #explore the closest node
            
            print(current)
            print(least)

            self.graph.remove(least)
            current = least
            total +=leastDist
            print(leastDist)
            print(total)

            leastDist = sys.float_info.max 
            least = None
        total +=self.dist(first, current)
        return total
            

def greedyTSP(link):
    #initialize two lists

    unexplored = Data()
    #explor the first node
    totalDistance = 0
    #loop until all nodes are explored
    dist = unexplored.explore(link)
    totalDistance += dist
        #print(totalDistance)
        #print(len(explored.graph))

    return totalDistance


print("answer: ", greedyTSP("greedyTSP.txt"))
