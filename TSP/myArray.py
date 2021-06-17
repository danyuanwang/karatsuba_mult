INF = 99999999999999
from node import Node
def toBinary(num, out):
    if num >1:
        toBinary(num//2, out)
    out.insert(0, num%2)
    
class Array:
    def __init__(self, n):
        self.nodes = n
        #self.array = [INF] * (n * (2**n))
        #self.array = SqliteDict('./my_db.sqlite', autocommit=True)
        self.array = {}
    def __str__(self):
        out = ""
        for i in self.array:
            out += str(i)
            out += " "

        return out
    #j is a node
    #gets the shortest path from to j through S
    def get(self, j, S):
        x = j.index
        y = self.toNum(S)
        key = (y*self.nodes) + x
        #change these out when swithcing between array and dict
        if key in self.array:
            return self.array[key]
        return INF

    def set(self, j, S, value):
        x = j.index
        y = self.toNum(S)
        key = (y*self.nodes) + x
        #print(key)
        self.array[key] = value

    #S is a path turns a path into a number
    def toNum(self, S):
        binary = [0] * self.nodes
        result = 0
        for i in S:
            binary[i.index] = 1
        for i in range(len(binary)):
            result += (2**i) * binary[i]
        return result
    #takes an index and turns it into the set of that index
    def toList(self, num):
        binary = []
        out = []
        toBinary(num, binary)
        
        for i in range(len(binary)):
            if(binary[i] == 1):
                out.append(i)
        return out
    