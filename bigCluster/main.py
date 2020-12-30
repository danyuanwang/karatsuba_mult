from ClustersClass import Clusters
from EdgesClass import Edges

def calculateBigClusters(dataFile):
    clusters = Clusters(dataFile)
    edgeList = Edges(dataFile)
    print(edgeList.edges[0])
    print(edgeList.edges[1])
    print(edgeList.edges[2])
    while len(edgeList.edges[2]) > 0:
        shortestEdge = edgeList.shortestEdge()
        clusters.combine(shortestEdge)
        print("clusters Remainging: ", clusters.clusterCount)
    return clusters.clusterCount

print(calculateBigClusters("dataBigCluster.txt"))