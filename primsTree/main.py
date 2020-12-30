from graph import Group
from edgeData import EdgeData
edgeData = EdgeData()
def main(edgeData):
    group1 = Group()
    group2 = Group()
    for edge in edgeData.data:
        group2.add(edge[0])
    group2.remove(edgeData.data[0][0])
    group1.add(edgeData.data[0][0])
    
    
    totalweight = 0
    while group2.size() > 0:
        connectionlist = edgeData.connections(group1)
        print(totalweight)
        print("nodes remaining: ", group2.size())
        edge = findleast(connectionlist)
        totalweight += edge[2]
        group1.add(edge[0])
        group1.add(edge[1])
        group2.remove(edge[0])
        group2.remove(edge[1])
    return totalweight

def findleast(input):
    min = input[0]
    for i in input:
        if i[2] < min[2]:
            min = i
    return min

answer = main(edgeData)
print(answer)