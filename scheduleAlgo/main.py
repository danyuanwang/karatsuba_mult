

def extract_file():
    handle = open("data.txt")
    graph = []
    for line in handle:
        
        list = [float(v) for v in line.split()]
        graph.append(list)
    return graph

def func(list):
    #not optimal way
    #return (list[0] - list[1])* 1000000 + list[0]
    #optimal way
    return (list[0] / list[1])

def sortList(list):
    final = sorted(list, key = func, reverse = True)
    return final

def calculateCompTime(list):
    list.pop(0)
    sortedList = sortList(list)
    time = 0
    weightedSum = 0
    for task in sortedList:
        time += task[1]
        weightedSum += task[0] * time
    return weightedSum
data = extract_file()
print(calculateCompTime(data))
