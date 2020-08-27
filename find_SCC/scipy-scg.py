import numpy as np
from scipy.sparse import csr_matrix, coo_matrix
from scipy.sparse.csgraph import connected_components, dijkstra
def read_file():
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
    return coo_matrix((dn, (tn, hn)), shape=(lenght, lenght))

graph = read_file()
graph = csr_matrix(graph)
n_components, labels = connected_components(csgraph=graph, directed=False, return_labels=True)

print(n_components)
print(labels)
