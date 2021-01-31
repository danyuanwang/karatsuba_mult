import array
from bfgraph import BFGraph, INFPATH 
from cacheA import CacheA
class BFPath:
    def __init__(self, graph):
        self.graph = graph
        self.cacheA =  CacheA(self.graph.GetNumOfEdge(), self.graph.GetNumOfNode())

    def GetShortestPathFrom(self, s):
        shortest = INFPATH
        for v in self.graph.GetAllNodes():
            if(s == v): continue
            t = self.GetShortestPathBetween(s,v,self.graph.GetNumOfEdge())
            if(shortest > t):
                shortest = t
            break
        return shortest


    def GetShortestPathOfAll(self):
        shortest = INFPATH
        for s in self.graph.GetAllNodes():
            t = self.GetShortestPathFrom(s)
            if(shortest > t):
                shortest = t
            break
        return shortest

    def GetShortestPathBetween(self,s,v,i):
        if(s == v): return INFPATH
        if(i == 0): return INFPATH
        shortest = self.cacheA.GetFromCache(s, v, i)
        if(shortest <INFPATH): return shortest

        shortest =  self.graph.GetEdge(s,v)
        for w in self.graph.GetAdjacentNodes(s):
            d = self.graph.GetEdge(s, w)
            t = self.GetShortestPathBetween(w, v,  self.graph.GetNumOfEdge())
            if(t < INFPATH and shortest > t + d):
                shortest = t + d


        t =  self.GetShortestPathBetween(s,v,i-1)
        if(shortest > t):
            shortest = t

        self.cacheA.SetToCache(s,v,i,shortest) 
        return shortest


