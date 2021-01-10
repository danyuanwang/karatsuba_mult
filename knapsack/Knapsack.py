
empty = -1
class Knapsack():
    def __init__(self):
        self.knapCapacity = 10000
        self.itemCount = 100
        self.data = []
        handle = open('data.txt')
        flag = True
        for line in handle:
            if flag:
                flag = False
                continue
            list = [int(v) for v in line.split()]
            self.data.append(list)
        #print(self.data)


        self.array = []
        firstLine = [0] * (self.knapCapacity + 1)
        self.array.append(firstLine)


        

    def fillArray(self):
        for i in range(1, self.itemCount + 1):
            temp = [empty] * (self.knapCapacity + 1)
            self.array.append(temp)
            for j in range(0, self.knapCapacity + 1):
                self.array[i][j] = self.compareOptions(i, j)
        #print(self.array)
        return self.array[self.itemCount][self.knapCapacity]


    def compareOptions(self, itemIndex, capacity):
        option1 = self.array[itemIndex - 1][capacity]
        if (capacity - self.data[itemIndex - 1][1] < 0):
            return option1
        option2 = self.array[itemIndex - 1][capacity - self.data[itemIndex - 1][1]] + self.data[itemIndex - 1][0]
        return max(option1, option2)