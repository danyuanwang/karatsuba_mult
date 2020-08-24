# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import dmatrix
t = 0
#very self explanatory
def reverse_graph(graph, nodes):
    graph.transpose()
    graph.order(nodes)

    return new_graph

#loop to run dfs biggest loop
#will switch parent nodes on one runs out
def dfs_loop(graph):
# t is the ordering of the nodes(heads) for the second loop through
    global t
    t = 0
# i represents a node
    i = graph.size() - 1
# explored marks the already explored nodes so we don't explore them twice
    explored = []
#SCC marks the size of all the SCCs discovered (only useful for second run)
    SCC = []
    order = [0] * graph.size()
#loops through nodes, only stop at the nearest unexplored node 
    while i > 0:
        if i not in explored:

        #calculates the size of an SCC if found. also runs dfs to explore the nodes below parent
            t_pre = t
            # graph is the graph, i is the number of the node in order from start to end, explored is the explored nodes, order is the order it goes in(only useful for first run)
            dfs(graph, i, explored, order)

            t_post = t - t_pre
            SCC.append(t_post)

        i -= 1
    return order, SCC

#smaller recursive for dfs
#will explore form one parent node
def dfs(graph, i, explored, order):
    # t is the ordering of the nodes(heads) for the second loop through
    global t
    explored.append(i)
    for j in range(graph.size('h')):
        if graph.access(i, j) == 1:
            if j not in explored:
                dfs(graph, j, explored, order)
    #calculates t
    order[i] = t
    t += 1








def compute_scc(graph):
    # Use a breakpoint in the code line below to debug your script.
    graph = reverse_graph(graph, list(range(len(graph))))  # Press Ctrl+F8 to toggle the breakpoint.

    order, temp = dfs_loop(graph)
    graph = reverse_graph(graph, order)
    useless, SCC = dfs_loop(graph)

    return SCC


# Press the green button in the gutter to run the script.
graph = [
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]

list = compute_scc(graph)

list.sort()
for i in range(2):
    print(list.pop())