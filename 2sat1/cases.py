import math
class Cases:
    def __init__(self, link):
        self.size = 0
        self.cases = []
        handle = open(link)
        for line in handle:
            a = line.split()
            #print(a)
            res = [int(i) for i in a]
            self.cases.append(res)
            self.size += 1

        for j in range(5):
            for i in range(1, self.size + 1):
                print(j, i, len(self.cases)," init")
                firstValueFlag = True
                removeFlag = True
                value = i
                for case in self.cases:
                    if i in case and firstValueFlag == True:
                        firstValueFlag = False
                    elif -i in case and firstValueFlag == True:
                        firstValueFlag = False
                        value = -i
                    elif -value in case:
                        removeFlag = False
                        break
                if removeFlag:
                    for case in self.cases:
                        if i in case:
                            self.cases.remove(case)
            


                    



    #test one case in the set
    #true if the first value or the second value == true 
    #* negative indicates not
    def test_case(self, index, values):
        #print(int(self.cases[index][0]))
        value1 = values[abs(self.cases[index][0])]
        value2 = values[abs(self.cases[index][1])]
        if self.cases[index][0] < 0:
            value1 = not value1
        if self.cases[index][1] < 0:
            value2 = not value2

        return value1 or value2
        
    #test all cases using test above if there is one that evaluates to false return
    #that case, otherwise return -1
    def test_all_cases(self, values):
        for index in range(len(self.cases)):
            result = self.test_case(index, values)
            if not result:
                return index

        return -1
