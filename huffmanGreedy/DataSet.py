class DataSet():
    def __init__(self):
        self.data = {}
        self.tree = []

        handle = open('data.txt')
        counter = 0
        flag = True
        for line in handle:
            if flag:
                flag = False
                continue
            self.data[counter] = ([int(line)])
            self.tree.append(counter)
            counter += 1
        self.count = counter
        print(self.data[391])
        


    def combine(self, S1, S2):
        self.tree.append(self.count)
        self.data[self.count] = [self.data[S1][0] + self.data[S2][0], [S1, S2]]
        #print("adding,", self.data[S1][0] + self.data[S2][0], self.data[S1][0], self.data[S2][0] )
        self.count += 1
        

    def findSmallest(self):
        self.tree.sort(key = self.sortKey)
        S1 = self.tree.pop(0)
        S2 = self.tree.pop(0)
        return S1, S2

    def sortKey(self, input):
        return self.data[input][0]

    def Paths(self, node):
        #print("node:", node)
        if(len(self.data[node]) == 1):
            return 0, 0
        
        max = 0
        min = 0
        #print("Self data", self.data[node][1], node)
        Max1, Min1 = self.Paths(self.data[node][1][0])
        Max2, Min2 = self.Paths(self.data[node][1][1])
        
        
        if Max1 > Max2:
            max = Max1
        else:
            max = Max2
        if Min1 < Min2:
            min = Min1
        else:
            min = Min2
        print("Max, Min", max, min)
        return max + 1, min + 1
