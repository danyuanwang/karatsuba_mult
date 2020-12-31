import array
import sys
empty = (2<< 31) - 1
noparent = (2<< 31) - 2

class Clusters():

# input a file with data
    def __init__(self, cluster):
        self.cluster = cluster
        self.clusterCount = 2000
        print("finished Cluster Initializaton")

#input a edge consisting of a list with two strings representing nodes
    def combine(self, edge):
        cluster1 = self.findCluster(edge[0])
        cluster2 = self.findCluster(edge[1])
        if cluster1 == cluster2:
            return False
        self.cluster[cluster1] = cluster2
        self.cluster[edge[0]] = cluster2
        self.clusterCount -= 1
        return True
#input a string repersenting a node
    def findCluster(self, node):
        tested = node
        while self.cluster[tested] != noparent:
            tested = self.cluster[tested]

        return tested
