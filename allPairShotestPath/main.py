from paths import Paths
from bfpath import BFPath
from bfgraph import BFGraph
graph = BFGraph('test.txt')
bfpath = BFPath(graph)
answer=bfpath.GetShortestPathOfAll()

#Graph = Paths()
#answer = Graph.NodeShortest()
#for i in range(4):
#answer = Graph.getShortestDist(1, 2, 4)
print(answer)