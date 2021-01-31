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
            t, modified = self.GetShortestPathBetween(s,v,self.graph.GetNumOfEdge())
            if(shortest > t):
                shortest = t
            if(modified):
                print("modified")
                break
            #break
        return shortest, modified


    def GetShortestPathOfAll(self):
        shortest = INFPATH
        for s in self.graph.GetAllNodes():
            t, modified = self.GetShortestPathFrom(s)
            if(shortest > t):
                shortest = t
            if(modified):
                print("modified")
                break
            #break
        return shortest, modified

    def GetShortestPathBetween(self,s,v,i):
        if(s == v): return INFPATH, False
        if(i == 0): return INFPATH, False
        shortest = self.cacheA.GetFromCache(s, v, i)
        if(shortest <INFPATH): return shortest, False

        shortest =  self.graph.GetEdge(s,v)
        for w in self.graph.GetAdjacentNodes(s):
            d = self.graph.GetEdge(s, w)
            t = 0
            if w != v:
                t, temp3 = self.GetShortestPathBetween(w, v, i-1)
            if(t < INFPATH and shortest > t + d):
                shortest = t + d


        t1, temp2 =  self.GetShortestPathBetween(s,v,i-1)
        if(shortest > t1):
            shortest = t1

        modified = self.cacheA.SetToCache(s,v,i,shortest)
            
        return shortest, modified


