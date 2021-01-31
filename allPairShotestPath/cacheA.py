import array
from bfgraph import INFPATH 
class CacheA:
    def __init__(self, m, n):
        self.c = m + 1
        self.r = n
        self.cacheA = array.array('i')
        self.cacheA.extend((INFPATH,) * self.c * self.r)

    def GetFromCache(self, i, v):
        return self.cacheA[i * self.r + v]

    def SetToCache(self, i, v, value):
        modified = False
        original = self.GetFromCache(i, v)
        if value < original:
            self.cacheA[i * self.r + v] = value
            modified = True
        return modified
        
