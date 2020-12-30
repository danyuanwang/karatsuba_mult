class UnionFind():
    def __init__(self, nodeNumber):
        self.clusters = []
        for i in range(nodeNumber+1):
            self.clusters.append([i])
        #print(self.clusters)

    def find(self, node):
        #print("clusters node", self.clusters[node])
        tested = node
        while(len(self.clusters[tested]) > 1):
            #print("testedpre", self.clusters[tested])
            tested = self.clusters[tested][1]
            #print("tested", self.clusters[tested], node)
        return tested


    def combine(self, edge):
        #print("node", edge[0], edge[1])
        cluster1 = self.find(int(edge[0]))
        #print("first")
        cluster2 = self.find(int(edge[1]))
        #print("clusters", cluster1, cluster2)

        if cluster1 == cluster2:
            return False
        self.clusters[cluster2]. append(cluster1)

        return True
