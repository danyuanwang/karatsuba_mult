from edgeDatas import EdgeData
from UnionFindFile import UnionFind

def calculateClusters(edgeData):
    edgeData.data.sort(key = sortKey)
    nodeCount = edgeData.nodeCount
    nodes = UnionFind(nodeCount)
    while(nodeCount > 4):
        shortestEdge = edgeData.data.pop(0)
        print(shortestEdge)
        flag = nodes.combine(shortestEdge)
        if flag:
            nodeCount -= 1
        print(nodeCount)

    #print(nodes.clusters)
    for i in range(len(nodes.clusters)):
        if (len(nodes.clusters[i]) == 1):
            print(nodes.clusters[i])
            
    shortestEdge = edgeData.data.pop(0)
    while(nodes.combine(shortestEdge) == False):
        shortestEdge = edgeData.data.pop(0)

    print(shortestEdge)
def sortKey(list):
    return list[2]


edgeData = EdgeData("data.txt")
calculateClusters(edgeData)
