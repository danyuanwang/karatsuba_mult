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
    def printArr(self, dist):  
        print("Vertex Distance from Source")  
        for i in range(self.V):  
            print("{0}\t\t{1}".format(i, dist[i]))  
      
    # The main function that finds shortest distances from src to  
    # all other vertices using Bellman-Ford algorithm. The function  
    # also detects negative weight cycle  
    def BellmanFord(self, src):  
  
        # Step 1: Initialize distances from src to all other vertices  
        # as INFINITE  
        dist = [float("Inf")] * self.V  
        dist[src] = 0
  
  
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
  
        # Step 3: check for negative-weight cycles. The above step  
        # guarantees shortest distances if graph doesn't contain  
        # negative weight cycle. If we get a shorter path, then there  
        # is a cycle.  
  
        for u, v, w in self.graph:  
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                        print("Graph contains negative weight cycle") 
                        return
                          
        # print all distance  
        self.printArr(dist) 
firstline = True
handle = open("test.txt")
for line in handle:
    list = [int(v) for v in line.split()]
    if firstline:
        #[nodeCount, edgeCount] = list
        g = Graph(4)  
    else:
        g.addEdge(list[0], list[1], list[2]) 
  
# Print the solution  
g.BellmanFord(0)  
  
# Initially, Contributed by Neelam Yadav  
# Later On, Edited by Himanshu Garg 