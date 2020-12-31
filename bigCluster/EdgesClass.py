import time


empty = 2** 31 - 1
noparent = 2** 31 - 2
class Edges():
    def __init__(self, data, dataSpace):
        self.edges = [[], [], []]
        self.data = data
        self.dataSpace = dataSpace
        nodeFinished = 0
        for node in self.data:
            startTime = time.time()

            self.hammingCircle(node)
            endTime = time.time()
            nodeFinished +=1
            timeElapsed = endTime - startTime

            print(nodeFinished, timeElapsed)
        
        print("Finished Edges Initialization")
        #for node1 in self.data:
         #   for node2 in self.data:
                #print("lines read: ", line1, line2)
           #     if self.hammingDist(node1, node2) == 3:
            #        self.edges[2].append([node1, node2])
             #   elif self.hammingDist(node1, node2) == 2:
              #      self.edges[1].append([node1, node2])
              #  elif self.hammingDist(node1, node2) == 1:
               #     self.edges[0].append([node1, node2])
        #print(comparisonsMade)


    def shortestEdge(self):
        for edgeGroup in self.edges:
            if len(edgeGroup) > 0:
                return edgeGroup.pop(0)

    def hammingDist(self, node1, node2):
        count = 0
        #print("comparing:", node1, node2)
        result = node1 ^ node2
        while(result != 0):
            result = result & (result-1)
            count += 1
        #print("count:", node1, node2, count)
        return count

    def hammingCircle(self, node1):

        flip1 = 1
        for i in range(1, 25):
            
            nodeNew1 = node1 ^ flip1
            flip1 <<= 1
            #print(nodeNew1)
            #print("nodeNew1", nodeNew1)
            if self.dataSpace[nodeNew1] != empty:
                #print("placed11")
                self.edges[0].append([nodeNew1, node1])

            flip2 = flip1
            for j in range(1, 24 - i):
                flip2 <<= 1
                if flip1 != flip2:
                    nodeNew2 = nodeNew1 ^ flip2
                    
                    if self.dataSpace[nodeNew2] != empty:
                        #print("placed222222222222222222222222222")
                        self.edges[1].append([nodeNew2, node1])

                    flip3 = flip2
                    for h in range(1, 24 - j - i):
                        flip3 <<= 1
                        if flip3 != flip1 and flip3 !=flip2:
                            nodeNew3 = nodeNew2 ^ flip3
                            
                            #print(nodeNew3)
                            if self.dataSpace[nodeNew3] != empty:
                                #print("placed333333333333333333333333333333333333333333333333333333333333")
                                self.edges[2].append([nodeNew3, node1])