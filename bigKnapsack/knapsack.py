import array
empty = -1
def combineNote(n1, n2):
    return (n1<<32) + n2
def decombineNodes(n):
    return [n>>32,n&0xffffffff]
class Knapsack():
    def __init__(self):
        handle = open('databig.txt')

        self.data = [empty]
        self.instanceStorage = {}
        firstline = True
        for line in handle:
            list = [int(v) for v in line.split()]
            if firstline:
                [self.knapCapacity, self.itemCount] = list
                firstline = False
            else:
                self.data.append(list)

            
    def findOptimum(self, itemCount, knapCapacity):
        key = combineNote(itemCount,knapCapacity)
        if key in self.instanceStorage:
            return self.instanceStorage[key]
        
        r = 0
        if itemCount == 0:
            r = 0
        else:
            option1 = 0
            option2 = 0

            option1 = self.findOptimum(itemCount - 1, knapCapacity)

            if self.data[itemCount][1] > knapCapacity:
                r = option1

            else:
                option2 = self.findOptimum(itemCount - 1, knapCapacity - self.data[itemCount][1]) + self.data[itemCount][0]
                r = max(option1, option2)

        print(itemCount, knapCapacity)
        self.instanceStorage[key] = r

        return r
        
