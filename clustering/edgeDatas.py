class EdgeData():
    def __init__(self, dataFile):
        handle = open(dataFile)
        self.data = []
        for line in handle:
            
            list = [float(v) for v in line.split()]
            self.data.append(list)
        self.nodeCount = int(self.data.pop(0)[0])
        print(self.nodeCount)

    def findEdge(self, node1, node2):
        for i in self.data:
            if i[0] == node1:
                if i[1] == node2:
                    return i
            elif i[0] == node2:
                if i[1] == node1:
                    return i
        return None

    def testStreches(self, edge, group1):
        found1 = False
        found2 = False
        for i in group1.list:
            if(i == edge[0]):
                found1 = True

            elif(i == edge[1]):
                found2 = True
        return found1 ^ found2


    def connections(self, group1):
        connectionList = []
        for i in self.data:
            result = self.testStreches(i, group1)
            if result:
                connectionList.append(i)
        return connectionList
