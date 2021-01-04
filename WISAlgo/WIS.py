import array
empty = (2<< 31) - 1
class WIS():
    def __init__(self):
        self.data = []
        self.records = {}
        handle = open('data2.txt')
        flag = True
        for line in handle:
            if flag:
                flag = False
                continue
            self.data.append(int(line))
    def findWIS(self, n):
        if n == 0:
            self.records[n] = [self.data[n], n]
            return [self.data[n], n]
        if n == 1:
            if self.data[0] > self.data[1]:
                self.records[n] = [self.data[0], n-1]
                return [self.data[0], n-1]
            self.records[n] = [self.data[1], n]
            return [self.data[1], n]
        ExcludeW = None
        IncludeW = None
        print("weights:", n, self.data[n])
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
        IncludeW[0] += self.data[n]
        IncludeW.append(n)

        if ExcludeW[0] > IncludeW[0]:
            self.records[n] = ExcludeW
            print("returned excluded", n, ExcludeW, self.records)
            return ExcludeW
        self.records[n] = IncludeW
        print("returned included", n, IncludeW, self.records)
        return IncludeW