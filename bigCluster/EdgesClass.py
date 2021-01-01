import time
empty = (2<< 31) - 1
noparent = (2<< 31) - 2
def combineNote(n1, n2):
    return (n1<<32) + n2
def decombineNodes(n):
    return [n>>32,n&0xffffffff]

class Edges():
    def __init__(self, data, dataSpace):
        self.edges = [set(), set(), set()]
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
                return decombineNodes(edgeGroup.pop())

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
        for i in range(1, 5):
            
            nodeNew1 = node1 ^ flip1
            #print("nodeNew1", bin(nodeNew1), bin(node1), bin(flip1))
            
            #print(nodeNew1)
            #print("nodeNew1", nodeNew1)
            if self.dataSpace[nodeNew1] != empty:
                h= self.hammingDist(nodeNew1,node1)
                if(h!=1):
                    print("ERROR:hammingDist should be 1", bin(nodeNew1),bin(node1), h, bin(flip1))
                n1= max(nodeNew1,node1)
                n2 = min(nodeNew1,node1)
                self.edges[0].add(combineNote(n1, n2))
                #print("edge Found 1", bin(nodeNew1), bin(node1), combineNote(n1, n2), decombineNodes(combineNote(n1, n2)))

            flip2 = flip1 << 1
            for j in range(1, 5 - i):
                
                if flip1 != flip2:
                    nodeNew2 = nodeNew1 ^ flip2
                    #print("nodeNew2", bin(nodeNew2), bin(nodeNew1), bin(flip2))
                    
                    if self.dataSpace[nodeNew2] != empty:
                        h= self.hammingDist(nodeNew2,node1)
                        if(h!=2):
                            print("ERROR:hammingDist should be 2", bin(nodeNew2),bin(node1), h)
                        n1= max(nodeNew2,node1)
                        n2 = min(nodeNew2,node1)
                        self.edges[1].add(combineNote(n2, n1))
                        #print("edge Found 2", bin(nodeNew2), bin(node1), combineNote(n2, n1), decombineNodes(combineNote(n2, n1)))
                

                    flip3 = flip2 << 1
                    for c in range(1, 5 - j - i):
                        if flip3 != flip1 and flip3 !=flip2:
                            nodeNew3 = nodeNew2 ^ flip3
                            #print("nodeNew3", bin(nodeNew3), bin(nodeNew2), bin(flip3))
                            #print(nodeNew3)
                            if self.dataSpace[nodeNew3] != empty:
                                h= self.hammingDist(nodeNew3,node1)
                                if(h!=3):
                                    print("ERROR:hammingDist should be 3", bin(nodeNew3),bin(node1), h)
                                n1= max(nodeNew3,node1)
                                n2 = min(nodeNew3,node1)
                                self.edges[2].add(combineNote(n2, n1))
                                #print("edge Found 3", bin(nodeNew3), bin(node1), combineNote(n2, n1), decombineNodes(combineNote(n2, n1)))
                        flip3 <<= 1
                flip2 <<= 1
            flip1 <<= 1