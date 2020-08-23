from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

graph = []

handle = open('Find_SCC_data.txt')
for line in handle:
    t , h = [int(float(v)) for v in line.split()]
    while(h >= len(graph) or graph[h] == None):
        graph.insert(h,[])

    while(t >= len(graph[h])):
        graph[h].insert(t , 0)
    
    graph[h][t] = 1

print(len(graph), len(graph[0]))

graph = csr_matrix(graph)

print(graph)

n_components, labels = connected_components(csgraph=graph, directed=False, return_labels=True)

print(n_components)
print(labels)
