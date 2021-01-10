import array
empty = -1
def combineNote(n1, n2):
    return (n1<<32) + n2
def decombineNodes(n):
    return [n>>32,n&0xffffffff]
class Knapsack():
    def __init__(self):
        self.knapCapacity = 5
        self.itemCount = 5
        self.data = [empty]
        self.instanceStorage = {}
        #self.instanceStorage.extend((empty,) * (2000000 * 2000))
        handle = open('test.txt')
        flag = True
        for line in handle:
            if flag:
                flag = False
                continue
            list = [int(v) for v in line.split()]
            self.data.append(list)

            
    def findOptimum(self, itemCount, knapCapacity):
        if itemCount == 0:
            return 0
        option1 = 0
        option2 = 0

        if(combineNote(itemCount - 1, knapCapacity) not in self.instanceStorage):
            option1 = self.findOptimum(itemCount - 1, knapCapacity)
            self.instanceStorage[combineNote(itemCount - 1, knapCapacity)] = option1
        else:
            option1 = self.instanceStorage[combineNote(itemCount - 1, knapCapacity)]

        if self.data[itemCount][1] > knapCapacity:
            return option1

        if(combineNote(itemCount - 1, knapCapacity - self.data[itemCount][1]) not in self.instanceStorage):
            option2 = self.findOptimum(itemCount - 1, knapCapacity - self.data[itemCount][1]) + self.data[itemCount][0]
            self.instanceStorage[combineNote(itemCount - 1, knapCapacity - self.data[itemCount][1])] = option2
        else:
            option2 = self.instanceStorage[combineNote(itemCount - 1, knapCapacity - self.data[itemCount][1])]
        return max(option1, option2)
        
