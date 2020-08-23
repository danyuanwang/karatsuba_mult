# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

def extract_file():
    handle = open('Graph_data.txt')
    graph = []
    for line in handle:
        list = [float(v) for v in line.split()]
        graph.append(list)
    return graph

def contraction(list):
    point1 = random.choice(list)
    point1_first = point1.pop(0)
    #print("list:", list)
    point2 = random.choice(point1)
    #print(point1)
    point1.insert(0, point1_first)
    #print(point1, point2)
    #append the merged vertice and pop it from graph
    for i in range(len(list)):
        #print(i)
        if list[i][0] == point2:
            point1.extend(list[i])


            #only a single occurance per loop so is fine
            list.pop(i)
            #print(point1)
            #print('popped', list)
            break
    #organize the edges after vertices are merged

    #loop over the entire graph
    for i in range(len(list)):

        # eliminate self loops looping backwards to prevent the pop function from changing the index as we loop
        #also cleverly avoids first
        j = 1
        while j < (len(list[i])):
            # replace the merged vertice with the vertice it was absorbed by
            if list[i][-j] == point2:
                list[i][-j] = point1[0]

            # eliminate self loops
            if list[i][-j] == list[i][0]:
                list[i].pop(-j)
                j -= 1
            #incremnts
            j += 1









def find_min_cut(graph):
    # Use a breakpoint in the code line below to debug your script.
    #print(graph)
    #print('break')
    while len(graph) > 2:

        contraction(graph)
        #print(graph)
        #print('break')

    return len(graph[0]) - 1



graph = [
    [1, 2, 3, 4],
    [2, 1, 4],
    [3, 1, 4],
    [4, 1, 2, 3]
]
graph1 = extract_file()
print(graph1)
lowest = 100000000000000000000000000000
cut = 0
for num in range(10):
    graph1 = extract_file()
    cut = find_min_cut(graph1)
    #print(cut)
    if cut < lowest:
        lowest = cut
        #print('lowest', lowest)
#print('answer')
print(lowest)

# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/