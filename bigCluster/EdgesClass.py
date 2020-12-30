import time
class Edges():
    def __init__(self, dataFile):
        self.edges = [[], [], []]
        handle = open(dataFile)
        self.data = []
        self.dataSpace = {}
        for line in handle:
            self.data.append(line)
        self.data.pop(0)
        for node in self.data:
            self.dataSpace[node] = 0
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
        for i in range(len(node1)):
            if(node1[i] != node2[i]):
                count += 1
        #print("count:", node1, node2, count)
        return count

    def hammingCircle(self, node1):

        for i in range(len(node1)):
            nodeNew1 = self.modify(node1, i)
            #print(nodeNew1)
            if nodeNew1 in self.dataSpace:
                self.edges[0].append(nodeNew1)
            for j in range(len(nodeNew1)):
                if j != i:
                    nodeNew2 = self.modify(nodeNew1, j)
                    if nodeNew2 in self.dataSpace:
                        self.edges[1].append(nodeNew2)
                    for h in range(len(nodeNew2)):
                        if h != j and h !=i:
                            nodeNew3 = self.modify(nodeNew2, h)
                            if nodeNew3 in self.dataSpace:
                                self.edges[2].append(nodeNew3)



    def modify(self, string, index):
        result = list(string)
        if result[index] == "0":
            result[index] == "1"
        else:
            result[index] = "0"
        result = "".join(result)
        return result