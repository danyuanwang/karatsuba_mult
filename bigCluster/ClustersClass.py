class Clusters():

# input a file with data
    def __init__(self, data):
        self.cluster = {}
        self.clusterCount = 200000
        handle = open(data)
        flag = True
        
        for line in handle:
            if flag:
                flag = False
                print(self.clusterCount)
                continue
            #list = [float(v) for v in line.split()]
            self.cluster[line] = ""
        print("finished Cluster Initializaton")

#input a edge consisting of a list with two strings representing nodes
    def combine(self, edge):
        cluster1 = self.findCluster(edge[0])
        cluster2 = self.findCluster(edge[1])
        if cluster1 == cluster2:
            return False
        self.cluster[cluster1] = cluster2
        self.clusterCount -= 1
        return True
#input a string repersenting a node
    def findCluster(self, node):
        tested = node
        while self.cluster[tested] != "":
            tested = self.cluster[tested]

        return tested
