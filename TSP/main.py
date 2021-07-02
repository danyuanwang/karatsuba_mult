from data import Data
from myArray import Array
import sys
INF = 99999999999999
print(sys.getrecursionlimit())
sys.setrecursionlimit(3000)


def main(file):
    #initializes the data and the array
    data = Data(file)
    array = Array(data.size)
    array.set(data.graph[0], [data.graph[0]], 0)
    #fills out array using data
    for j in range(data.size):
        runCase(array, data, data.graph, data.graph[j])
        print(j)
    min = INF

    #loop every possible last node
    for j in range(1, data.size):
        #calcuate the total distance from the Salesman tour and the last node + the last node to the first
        dist1 = array.get(data.graph[j], data.graph)
        dist2 = data.dist(data.graph[j], data.graph[0])
        distFinal = dist1 + dist2
        print("final:", j, dist1, dist2)
        if(distFinal < min):
            min = distFinal
    return min
#finds shortest distance fron 0 to j that goes through everything in S exactly once
def runCase(array, data, S, j):
    #S2 is the removed S
    S2 = [] + S
    #S2 is S without the destination j
    S2.remove(j)
    
    min = INF
    if(S2 == []):
        return data.dist(data.graph[0], j)
    for k in S2:
        #shortest path from 0 to K on S-j
        shortestK = array.get(k, S2)
        #if shortestK is not yet found find the shortest path
        if(shortestK == INF):
            shortestK = runCase(array, data, S2, k)

        #the shortest path from 0 to k + k to J
        shortestJ = shortestK + data.dist(j,k)
        #if k is the last node with the shortest path, record it in min
        if(shortestJ < min):
            min = shortestJ
    #then record it in the array
    array.set(j, S, min)
    return min

print(main("test.txt"))