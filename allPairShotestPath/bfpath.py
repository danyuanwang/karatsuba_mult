import array
from bfgraph import BFGraph, INFPATH 
from cacheA import CacheA
import time
class BFPath:
    def __init__(self, graph):
        self.graph = graph

    def GetShortestPathFrom(self, s):
        shortest = INFPATH
        cacheA =  CacheA(self.graph.GetNumOfNode())
        n = self.graph.GetNumOfEdge()
        startTime = time.time()
        for i in range(n):
            stopEarly = True
            for v in self.graph.GetAllNodes():
                if(s == v): 
                    cacheA.SetToCache(i, v, 0)
                elif(i == 0): 
                    cacheA.SetToCache(i, v,INFPATH)
                else:
                    shortest=cacheA.GetFromCache(i-1, v)
                    
                    for w in self.graph.GetPrecedentNodes(v):
                        t = cacheA.GetFromCache(i-1, w) + self.graph.GetEdge(w, v)
                        if(shortest > t) : shortest = t
                    #print("short", shortest, s, v, i)
                    cacheA.SetToCache(i, v,shortest)

                if(cacheA.GetFromCache(i-1, v) != cacheA.GetFromCache(i, v)) : 
                    stopEarly = False
            if(stopEarly): break


        print(time.time()-startTime, stopEarly, shortest)
        negativeCycledetected = False
        for v in self.graph.GetAllNodes():
            #print (n-1, v, cacheA.GetFromCache(n-2, v), cacheA.GetFromCache(n-1, v))
            if(cacheA.GetFromCache(n-2, v) != cacheA.GetFromCache(n-1, v)):
                negativeCycledetected = True
                break
        #print("result              ", shortest, negativeCycledetected)
        return shortest, negativeCycledetected


    def GetShortestPathOfAll(self):
        shortest = INFPATH
        negativeCycledetected = False
        #print(self.graph.GetAllNodes())
        for s in self.graph.GetAllNodes():
            print(s)
            t, negativeCycle = self.GetShortestPathFrom(s)
            if(shortest > t):
                shortest = t
            if negativeCycle == True:
                negativeCycledetected = True
                break
            #break
        print(s,shortest,negativeCycledetected)
        return shortest, negativeCycledetected



