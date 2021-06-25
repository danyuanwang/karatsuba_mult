from data import Data
def greedyTSP(link):
    #initialize two lists
    unexplored = Data()
    unexplored.getData(link)
    explored = Data()
    #explor the first node
    nodetemp = unexplored.graph.pop(0)
    explored.addNode(nodetemp)
    totalDistance = 0
    #loop until all nodes are explored
    while(len(unexplored.graph) > 0):
        dist = explored.explore(unexplored)
        totalDistance += dist
        #print(totalDistance)
        print(len(explored.graph))

    totalDistance += explored.dist(explored.currentNode, nodetemp)
    return totalDistance


print("answer: ", greedyTSP("greedyTSP.txt"))
