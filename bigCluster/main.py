from ClustersClass import Clusters
from EdgesClass import Edges
import array
import sys
import time
empty = (2<< 31) - 1
noparent = (2<< 31) - 2

def countCluster(cluster):
    i=0
    for c in cluster:
        if(c==noparent):
            i+=1
    return i

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
        if cluster[number] == empty:
            cluster[number] = noparent
            
        data[count]=number
        count+=1

    clusters = Clusters(cluster,countCluster(cluster))
    edgeList = Edges(data, cluster)
    #print("len(edgeList.edges[0])",len(edgeList.edges[0]), edgeList.edges[0])
    #print("len(edgeList.edges[1])",len(edgeList.edges[1]), edgeList.edges[1])
    #print("len(edgeList.edges[2])",len(edgeList.edges[2]), edgeList.edges[2])
    for i in range(2):
        while len(edgeList.edges[i]) > 0:
            startTime = time.time()
            shortestEdge = edgeList.shortestEdge()
            shortestEdgeElapsed = time.time()-startTime

            startTime = time.time()
            clusters.combine(shortestEdge)
            combineEdgeElapsed = time.time()-startTime

            print("clusters Remainging: ", clusters.clusterCount, len(edgeList.edges[0]), len(edgeList.edges[1]), len(edgeList.edges[2]), shortestEdgeElapsed, combineEdgeElapsed)
    doubleCheck = 0
    for i in range(len(cluster)):
        if(cluster[i] == noparent):
            #print("cluster:", i)
            doubleCheck += 1
    
    print("double checked answer:", doubleCheck)
    return clusters.clusterCount

startTime = time.time()
cluster = calculateBigClusters("dataBigCluster.txt")
print()
print(cluster, time.strftime("%H:%M:%S", time.gmtime(time.time()-startTime)))