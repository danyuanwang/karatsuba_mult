from cases import Cases
from values import Values
import math
import random
from datetime import datetime

def test_case(index, values, cases):
    #print(int(self.cases[index][0]))
    value1 = values[abs(cases[index][0])]
    value2 = values[abs(cases[index][1])]
    if cases[index][0] < 0:
        value1 = not value1
    if cases[index][1] < 0:
        value2 = not value2
    return value1 or value2

def twoSAT(link):
    cases = []
    size = 0
    handle = open(link)
    for line in handle:
        a = line.split()
        res = [int(i) for i in a]
        cases.append(res)     
        size+=1
    for j in range(5):
        for i in range(1, size + 1):
            firstValueFlag = True
            removeFlag = True
            value = i
            for case in cases:
                if i in case and firstValueFlag == True:
                    firstValueFlag = False
                elif -i in case and firstValueFlag == True:
                    firstValueFlag = False
                    value = -i
                elif -value in case:
                    removeFlag = False
                    break
                if removeFlag:
                    for case in cases:
                        if i in case:
                            cases.remove(case)
    size = len(cases)
    values = [False] * size
    print("size:", size)
    for i in range(int(math.log(size, 2))):
        for j in range(size):
            values[j] = random.choice([True, False])
        
        print(i)
        print(datetime.now().strftime("%H:%M:%S"))

        for j in range(int((size ** 2) * 2)):
            halt = False
            indextemp = 0
            for index in range(len(cases)):
                result = test_case(index, values, cases)
                if not result:
                    halt = True
                    indextemp = index
                    break
            if (halt == True):
                pos = int(random.choice(cases[indextemp]))
                values[pos-1] = not values[pos-1]
            else:
                return True
    return False

print(twoSAT("case1.txt"))
