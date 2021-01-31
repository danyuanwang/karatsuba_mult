import array
from bfgraph import BFGraph, INFPATH 
from cacheA import CacheA
import time
class BFPath:
    def __init__(self, graph):
        self.graph = graph

    def GetShortestPathFrom(self, s):
        shortest = INFPATH
        cacheA =  CacheA(self.graph.GetNumOfEdge(), self.graph.GetNumOfNode())
        n = self.graph.GetNumOfEdge() -1 
        startTime = time.time()
        for i in range(n):
            stopEarly = True
            for v in self.graph.GetAllNodes():
                if(s == v): 
                    cacheA.SetToCache(i,v,0)
                elif(i == 0): 
                    cacheA.SetToCache(i,v,INFPATH)
                else:
                    shortest=cacheA.GetFromCache(i-1,v)
                    for w in self.graph.GetPrecedentNodes(v):
                        t = cacheA.GetFromCache(i-1,w) + self.graph.GetEdge(w, v)
                        if(shortest > t) : shortest = t
                    cacheA.SetToCache(i,v,shortest)

                if(cacheA.GetFromCache(i,v) != cacheA.GetFromCache(i-1,v)) : 
                    stopEarly = False
                    
            if(stopEarly): break


        print(time.time()-startTime, stopEarly, shortest)
        negativeCycledetected = False
        for v in self.graph.GetAllNodes():
            if(cacheA.GetFromCache(n,v) != cacheA.GetFromCache(n-1,v)):
                negativeCycledetected = True
                break
        return shortest, negativeCycledetected


    def GetShortestPathOfAll(self):
        shortest = INFPATH
        negativeCycledetected = False
        for s in self.graph.GetAllNodes():
            t, negativeCycledetected = self.GetShortestPathFrom(s)
            if(shortest > t):
                shortest = t
        print(s,shortest,negativeCycledetected)
        return shortest, negativeCycledetected



