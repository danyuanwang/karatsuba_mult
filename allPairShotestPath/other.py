# Python3 program for Bellman-Ford's single source  
# shortest path algorithm.  
  
# Class to represent a graph  
class Graph:  
  
    def __init__(self, vertices):  
        self.V = vertices # No. of vertices  
        self.graph = []  
  
    # function to add an edge to graph  
    def addEdge(self, u, v, w):  
        self.graph.append([u, v, w])  
          
    # utility function used to print the solution  
    def findShortestArr(self, dist, predecssor):  
        
        shortest = dist[0]
        print("Vertex Distance from Source")  
        v = 0
        for i in range(self.V):  
            if(shortest> dist[i]):
                shortest = dist[i]
                v = i
        print("{0}\t\t{1}".format(v, dist[v]))  
        while predecssor[v] != float("Inf") :
            print(v, ":", dist[v])
            v = predecssor[v]


        return shortest
      
    # The main function that finds shortest distances from src to  
    # all other vertices using Bellman-Ford algorithm. The function  
    # also detects negative weight cycle  
    def BellmanFord(self, src):  
        # Step 1: Initialize distances from src to all other vertices  
        # as INFINITE  
        dist = [float("Inf")] * self.V  
        dist[src] = 0
        predecssor = [float("Inf")] * self.V  
  
  
        # Step 2: Relax all edges |V| - 1 times. A simple shortest  
        # path from src to any other vertex can have at-most |V| - 1  
        # edges  
        for _ in range(self.V - 1):  
            # Update dist value and parent index of the adjacent vertices of  
            # the picked vertex. Consider only those vertices which are still in  
            # queue  
            for u, v, w in self.graph:  
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                        dist[v] = dist[u] + w  
                        predecssor[v] = u
  
        # Step 3: check for negative-weight cycles. The above step  
        # guarantees shortest distances if graph doesn't contain  
        # negative weight cycle. If we get a shorter path, then there  
        # is a cycle.  
  
        for u, v, w in self.graph:  
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                        print("Graph contains negative weight cycle") 
                        return float("Inf")
                          
        # print all distance  
        return self.findShortestArr(dist, predecssor) 

firstline = True
nodeCount = 0
edgeCount = 0
handle = open("set3.txt")
for line in handle:
    list = [int(v) for v in line.split()]
    if firstline:
        [nodeCount, edgeCount] = list
        g = Graph(nodeCount)  
        firstline = False
    else:
        g.addEdge(list[0]-1, list[1]-1, list[2]) 

shortest = float("Inf")
# Print the solution  
#for s in range(nodeCount-1):
t = g.BellmanFord(398)  
if(shortest> t): shortest = t
#print(s,t, shortest)
print(shortest)
# Initially, Contributed by Neelam Yadav  
# Later On, Edited by Himanshu Garg 