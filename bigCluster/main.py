from ClustersClass import Clusters
from EdgesClass import Edges
import array
import sys
import time
empty = (2<< 31) - 1
noparent = (2<< 31) - 2

def calculateBigClusters(dataFile):

    cluster = array.array('I')
    cluster.extend((empty,) * (1<<24))
    data = array.array('I')
    data.extend((empty,) * 200000)

    handle = open(dataFile)
    flag = True
    count =0
    for line in handle:
        if flag:
            flag = False
            continue
        number = int(line.strip().replace(' ', ''), 2)
        #list = [float(v) for v in line.split()]
        cluster[number] = noparent

        data[count]=number
        count+=1

    clusters = Clusters(cluster)
    edgeList = Edges(data, cluster)
    print("len(edgeList.edges[0])",len(edgeList.edges[0]))
    print("len(edgeList.edges[1])",len(edgeList.edges[1]))
    print("len(edgeList.edges[2])",len(edgeList.edges[2]))
    while len(edgeList.edges[2]) > 0:
        startTime = time.time()
        shortestEdge = edgeList.shortestEdge()
        shortestEdgeElapsed = time.time()-startTime

        startTime = time.time()
        clusters.combine(shortestEdge)
        combineEdgeElapsed = time.time()-startTime

        print("clusters Remainging: ", clusters.clusterCount, len(edgeList.edges[0]), len(edgeList.edges[1]), len(edgeList.edges[2]), shortestEdgeElapsed, combineEdgeElapsed)
    return clusters.clusterCount

print(calculateBigClusters("dataBigCluster.txt"))