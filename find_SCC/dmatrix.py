import numpy as np
from scipy.sparse import csr_matrix, coo_matrix, csc_matrix

class DMatrix():
    def __init__(self):
        self.graph = {}
        self.order_v = []
        self.size_ = 0
        # handle = open('Find_SCC_data.txt')
        handle = open('Find_SCC_data.txt')
        for line in handle:
            t ,h  = [int(float(v)) for v in line.split()]    
            if(h not in self.graph.keys() or self.graph[h] == None):
                self.graph[h] = []
            self.graph[h].append(t)
            self.order_v.append(h)
            if(t > self.size_): self.size_ = t
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
        for t in self.graph.keys():
            for h in self.graph[t]:
                if h not in new_graph.keys():
                    new_graph[h] = []
                new_graph[h].append(t)
        self.graph = new_graph
        
        


    def traverse(self, order):
        for o in order:
            self.graph[o]



    def access(self, h, t):
        if h in self.graph.keys():
            for vt in self.graph[h]:
                if vt == t:
                    return 1
        return 0
        

    def size(self):
        return self.size_
        

    def printout(self):
        for k in self.graph.keys():
            print(k, self.graph[k])
    
    def gettails(self, h):
        #print("gettails:", h,self.graph.keys())
        if h in self.graph.keys():
            return self.graph[h]
        return []
