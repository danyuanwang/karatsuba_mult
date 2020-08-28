# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from dmatrix import DMatrix
import sys
sys.setrecursionlimit(1000000)
graph = DMatrix()

#very self explanatory
def reverse_graph(graph):
    graph.transpose()
    return graph

#loop to run dfs biggest loop
#will switch parent nodes on one runs out
def dfs_loop(graph, nodes):
# t is the ordering of the nodes(heads) for the second loop through
    c = 1
# explored marks the already explored nodes so we don't explore them twice
    explored = [0] * (graph.size() + 1)
#SCC marks the size of all the SCCs discovered (only useful for second run)
    SCC = []
    order = [0] * (graph.size())
    visited = []
#loops through nodes, only stop at the nearest unexplored node 
    #print("node:",len(nodes))
    for h in nodes:
        #print(h,len(explored))
        if explored[h] == 0:

        #calculates the size of an SCC if found. also runs dfs to explore the nodes below parent
            t_pre = len(visited)
            # graph is the graph, i is the number of the node in order from start to end, explored is the explored nodes, order is the order it goes in(only useful for first run)
            # print('next parent')
            vl = dfs(graph, h, explored)
            print("vl:", h, len(vl), vl)
            visited.extend(vl)
            SCC_size = len(visited) - t_pre
            SCC.append(SCC_size)

    for h in visited:  
        if(order[h - 1] == 0):
            order[h - 1] = c
            c += 1
        else:
            print("dup:", h, c)
    visited.clear()
    #print('order', order)

    return order, SCC

#smaller recursive for dfs
#will explore form one parent node
def dfs(graph, i, explored):
    # t is the ordering of the nodes(heads) for the second loop through
    stack = []
    visited = []
    h = i
    if(explored[h] == 1): return visited
  
    stack.append(h)

    while stack :
        h = stack.pop()
        #print("pop:s:", h, explored[h] , stack)        
        if( explored[h] == 0 ):
            explored[h] = 1 
            stack.append(h)
            #print("h:tails:", h, graph.gettails(h))
            for t in graph.gettails(h):
                if(explored[t] == 0):
                    stack.append(t)
            # dfs(graph, j, explored, order)
        else:
            visited.append(h)
            #print("visited:",h, visited)
    
    return visited
        


def proccess_order(order):
    new_order = [0] * len(order)
    for i in range(1, len(order) + 1):
        #print(order[i - 1])
        new_order[-(order[i - 1])] = i
    
    return new_order





def compute_scc(graph):
    # Use a breakpoint in the code line below to debug your script.
    graph.printout()
    print('')
    graph = reverse_graph(graph)  # Press Ctrl+F8 to toggle the breakpoint.
    graph.printout()
    order = list(range(1, graph.size() + 1))
    order.reverse()
    
    order, temp = dfs_loop(graph, order)
    #print(order)
    graph = reverse_graph(graph)
    graph.printout()
    order = proccess_order(order)
    #print('order final', order)
    useless, SCC = dfs_loop(graph, order)

    return SCC


# Press the green button in the gutter to run the script.


result = compute_scc(graph)
result.sort()

#print(result)
resultLen = len(result) 
count = 1
while count <= 7 and count <= resultLen:
   print(result[-count])
   count = count + 1
