from paths import Paths
from bfpath import BFPath
from bfgraph import BFGraph
import time

if __name__ == '__main__':
    graph = BFGraph('g1.txt')
    bfpath = BFPath(graph)

    startTime = time.time()
    answer, negativeCycledetected =bfpath.GetShortestPathOfAllMP()

    #Graph = Paths()
    #answer = Graph.NodeShortest()
    #for i in range(4):
    #answer = Graph.getShortestDist(1, 2, 4)
    print("shortest:",answer)
    print("negativeCycledetected:", negativeCycledetected)

    print(time.strftime("%H:%M:%S", time.gmtime(time.time()-startTime)))