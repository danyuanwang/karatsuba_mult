import array
empty = (2<< 31) - 1
class WIS():
    def __init__(self):
        self.data = []
        self.records = {}
        handle = open('data.txt')
        flag = True
        for line in handle:
            if flag:
                flag = False
                continue
            self.data.append(int(line))
            
    def findWIS(self, n):
        if n == 0:
            self.records[0] = [self.data[0], 0]
            return [self.data[0], 0]
        if n == 1:
            if self.data[0] > self.data[1]:
                self.records[1] = [self.data[0], 0]
                return [self.data[0], 0]
            self.records[1] = [self.data[1], 1]
            return [self.data[1], 1]
        ExcludeW = None
        IncludeW = None
        #print("weights:", n, self.data[n])
        if n-1 in self.records:
            ExcludeW = self.records[n-1]
        else:
            ExcludeW = self.findWIS(n-1)
            self.records[n-1] = ExcludeW

        if n-2 in self.records:
            IncludeW = self.records[n-2]
        else:
            IncludeW = self.findWIS(n-2)
            self.records[n-2] = IncludeW
        
        IncludeWTemp = []
        for i in IncludeW:
            IncludeWTemp.append(i)
        IncludeWTemp[0] += self.data[n]
        IncludeWTemp.append(n)

        if ExcludeW[0] > IncludeWTemp[0]:

            #print("returned excluded", n, ExcludeW, self.records)
            return ExcludeW
        #print("returned included", n, IncludeW, self.records)
        
        return IncludeWTemp