# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
t = 0

def reverse_graph(graph, nodes):
    hg = len(graph)
    wg = len(graph[0])
    transposed_graph = [[0 for x in range(wg)] for y in range(hg)]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            transposed_graph[j][i] = graph[i][j]

    print('transposed', transposed_graph)
    new_graph =[]

    for i in range(len(nodes)):
        new_graph.append(transposed_graph[nodes[-i]])
    print('new', new_graph)

    return new_graph


def dfs_loop(graph):
    global t
    t = 0
    i = len(graph) - 1
    explored = []
    SCC = []
    order = [0] * len(graph)
    while i > 0:
        if i not in explored:
            t_pre = t
            print('pre', t_pre)
            dfs(graph, i, explored, order)

            t_post = t - t_pre
            print('post', t, t_post)
            SCC.append(t_post)
        i -= 1
    return order, SCC


def dfs(graph, i, explored, order):
    global t
    explored.append(i)
    print('i', i)
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            if j not in explored:
                dfs(graph, j, explored, order)
    print('t', t)
    order[i] = t
    t += 1
    print(order)








def compute_scc(graph):
    # Use a breakpoint in the code line below to debug your script.
    graph = reverse_graph(graph, list(range(len(graph))))  # Press Ctrl+F8 to toggle the breakpoint.
    print('revers_graph', graph)
    order, temp = dfs_loop(graph)
    print('order', order)
    graph = reverse_graph(graph, order)
    print('final_graph', graph)
    useless, SCC = dfs_loop(graph)

    return SCC


# Press the green button in the gutter to run the script.
graph = [
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]
print('orig', graph)
list = compute_scc(graph)
print(list)
list.sort()
for i in range(2):
    print(list.pop())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
