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
        self.test=[1, 2, 3, 4, 17, 117, 517, 997]

    def findWIS(self, n):
        if n in self.records:
            return self.records[n]
        max = None
        if n == 0:
            max = [self.data[n], n]
        elif n == 1:
            max = [self.data[0], 0] if self.data[0] > self.data[1] else [self.data[1], 1]
        else:
            include = [] + self.findWIS(n-2)
            include[0] += self.data[n]
            include.append(n)

            exclude = [] + self.findWIS(n-1)

            max = exclude if exclude[0] > include[0] else include

        self.records[n] = max
        #print(n, max, self.records)

        return max
    
    def testWIS(self, max_sum):
        r = 0
        c = 0
        for t in self.test:
            if self.test[c] in max_sum:
                r+=(0x1<<c)
            c+=1
        return r