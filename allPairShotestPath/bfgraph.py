import array
INFPATH = 0x0FFFFFFF

class BFGraph:
    def __init__(self, filename):
        firstline = True
        self.nodeCount = 0
        self.edgeCount = 0
        handle = open(filename)
        for line in handle:
            list = [int(v) for v in line.split()]
            if firstline:
                [self.nodeCount, self.edgeCount] = list
                self.edges = array.array('i')
                self.edges.extend((INFPATH,) * self.nodeCount * self.nodeCount)
                self.nodes = {}
                firstline = False
            else:
                s = list[0] - 1
                v = list[1] - 1
                d = list[2]
                self.SetEdge(s, v, d)
                self.SetEdge(s, s, 0)
                self.SetEdge(v, v, 0)
                if(s in self.nodes):
                    self.nodes[s].append(v)
                else:
                    self.nodes[s] = [v]


    def SetEdge(self, s, d, w):
        self.edges[self.CombineKey(s,d)] = w

    def GetEdge(self, s, d):
        return self.edges[self.CombineKey(s,d)]
    def CombineKey(self, s, d):
        return s*self.nodeCount+d

    def GetNumOfNode(self):
        return self.nodeCount

    def GetNumOfEdge(self):
        return self.edgeCount

    def GetAllNodes(self):
        return self.nodes
    
    def GetAdjacentNodes(self, s):
        return self.nodes[s]