import numpy as np
from scipy.sparse import csr_matrix, coo_matrix, csc_matrix
import sys
class DMatrix():
    def __init__(self):
        self.graph = {}
        self.size_ = 0
        # handle = open('test_data.txt')
        handle = open('dijkstra_Data.txt')
        for line in handle:
            
            a = line.split()
            h = int(a[0])    
            self.graph[h] = {}
            for i in range(1, len(a)):
                t, weight = [int(v) for v in a[i].split(',')]

                self.graph[h][t] = weight
            # if(t > self.size_): self.size_ = t
            if(h > self.size_): self.size_ = h
            
  #          tn[count] = t
   #         hn[count] = h
   #         dn[count] = 1
 #       data = {}
 #       lenght = (int)(863705  / 8)
 #       tn = np.ndarray(shape=(lenght), dtype=np.uint8)
 ##       hn = np.ndarray(shape=(lenght), dtype=np.uint8)
 #       dn = np.ndarray(shape=(lenght), dtype=np.uint8)
#        count = 0
  #      handle = open('Find_SCC_data.txt')
 #       for line in handle:
   #         t , h = [int(float(v)) for v in line.split()]    
  #          tn[count] = t
   #         hn[count] = h
   #         dn[count] = 1
   #     coo = coo_matrix((dn, (tn, hn)), shape=(lenght, lenght))
        # self.graph = csr_matrix(coo)
        # self.graph = csc_matrix(coo)

    def transpose(self):
        new_graph = {}
        for h in self.graph.keys():
            for t in self.graph[h]:
                if t not in new_graph.keys():
                    new_graph[t] = {}
                new_graph[t][h] = self.graph[h][t]
        self.graph = new_graph
        

    def traverse(self, order):
        for o in order:
            self.graph[o]



    def edge(self, h, t):
        try:
            return self.graph[h][t]
        except:
            return sys.maxsize

    def size(self):
        return self.size_
        

    def printout(self):
        for k in self.graph.keys():
            print(k, self.graph[k])
    
    def gettails(self, h):
        #print("gettails:", h,self.graph.keys())
        if h in self.graph.keys():
            return self.graph[h]
        return {}
