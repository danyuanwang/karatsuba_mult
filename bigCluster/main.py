from ClustersClass import Clusters
from EdgesClass import Edges
import array
import sys
EMPTY = 2** 31 - 1
NOPARENT = 2** 31 - 2

def calculateBigClusters(dataFile):

    cluster = array.array('I')
    cluster.extend((EMPTY,) * (1<<24))
    data = array.array('I')
    data.extend((EMPTY,) * 200000)

    handle = open(dataFile)
    flag = True
    count =0
    for line in handle:
        if flag:
            flag = False
            continue
        number = int(line.strip().replace(' ', ''), 2)
        #list = [float(v) for v in line.split()]
        cluster[number] = NOPARENT

        data[count]=number
        count+=1
    print("finished Cluster Initializaton")

    clusters = Clusters(cluster)
    edgeList = Edges(data, cluster)
    #print(edgeList.edges[0])
    #print(edgeList.edges[1])
    #print(edgeList.edges[2])
    while len(edgeList.edges[2]) > 0:
        shortestEdge = edgeList.shortestEdge()
        clusters.combine(shortestEdge)
        print("clusters Remainging: ", clusters.clusterCount)
    return clusters.clusterCount

print(calculateBigClusters("dataBigCluster.txt"))