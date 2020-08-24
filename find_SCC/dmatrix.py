import numpy as np
from scipy.sparse import csr_matrix, coo_matrix, csc_matrix

class DMatrix():
    def __init__(self):
        data = {}
        lenght = (int)(863705  / 8)
        tn = np.ndarray(shape=(lenght), dtype=np.uint8)
        hn = np.ndarray(shape=(lenght), dtype=np.uint8)
        dn = np.ndarray(shape=(lenght), dtype=np.uint8)
        count = 0
        handle = open('Find_SCC_data.txt')
        for line in handle:
            t , h = [int(float(v)) for v in line.split()]    
            tn[count] = t
            hn[count] = h
            dn[count] = 1
        coo = coo_matrix((dn, (tn, hn)), shape=(lenght, lenght))
        self.graph = csr_matrix(coo)
        # self.graph = csc_matrix(coo)

    def transpose(self):
        self.graph.transpose()

    def order(self, order):

        pass

    def access(self, x, y):
        pass

    def size(self, direction = 'h'):
        pass
