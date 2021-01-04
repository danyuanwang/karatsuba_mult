from DataSet import DataSet

def huffmanCode():
    dataSet = DataSet()
    while len(dataSet.tree) > 1:
        S1, S2 = dataSet.findSmallest()
        dataSet.combine(S1, S2)
    #print(dataSet.tree[0])
    return dataSet.Paths(dataSet.tree[0])

print(huffmanCode())