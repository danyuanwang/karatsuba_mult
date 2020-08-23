# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def reverse_graph(graph, nodes):
    new_graph =[]
    print(nodes)
    for i in range(len(nodes)):
        print(i)
        new_graph.append(graph[nodes[i]])
    print(new_graph)
    for i in range(len(new_graph)):
        for j in range(len(new_graph[i])):
           if new_graph[i][j] == 1:

                new_graph[i][j] = new_graph[j][i]
                print(i, j)
                new_graph[j][i] = 1
    return new_graph



def dfs_loop(graph):
    t = 0
    s = None
    i = len(graph)
    explored = []
    SCC = []
    order = [0] * len(graph)
    while i > 0:
        if i not in explored:
            s = i
            t_pre = t
            dfs(graph, i, explored, t, order)
            t_post = t - t_pre
            SCC.append(t_post)
        i -= 1
    return order, SCC

def dfs(graph, i, explored, t, order):
    explored.append(i)

    for j in range(len(graph)):
        if graph[i][j] == 1:
            if j not in explored:
                dfs(graph, j, explored, t, order)
    t += 1
    order[i] = t








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

compute_scc(graph)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
