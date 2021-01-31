import array
from bfgraph import INFPATH 
class CacheA:
    def __init__(self, m, n):
        self.w = m + 1
        self.h = n
        self.l = n
        self.cacheA = array.array('i')
        self.cacheA.extend((INFPATH,) * self.w * self.h * self.l)

    def GetFromCache(self, s, v, i):
        return self.cacheA[(v * self.w + i) * self.h + s]

    def SetToCache(self, s, v, i, value):
        modified = False
        original = self.GetFromCache(s, v, i)
        if value != original:
            self.cacheA[(v * self.w + i) * self.h + s] = value
            modified = True
        return modified
        
