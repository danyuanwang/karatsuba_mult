from paths import Paths
from bfpath import BFPath
from bfgraph import BFGraph
graph = BFGraph('g1.txt')
bfpath = BFPath(graph)
answer, negativeCycledetected =bfpath.GetShortestPathOfAll()

#Graph = Paths()
#answer = Graph.NodeShortest()
#for i in range(4):
#answer = Graph.getShortestDist(1, 2, 4)
print("shortest:",answer)
print("negativeCycledetected:", negativeCycledetected)