import array
from bfgraph import INFPATH 
class CacheA:
    def __init__(self, n):
        self.l = n
        self.cacheA = array.array('i')
        self.cacheA.extend((INFPATH,) * self.l *2 )

    def GetFromCache(self, j, v):
        return self.cacheA[ (j & 0x1 ) * self.l+ v]

    def SetToCache(self, j, v, value):
        self.cacheA[ (j & 0x1 ) * self.l+ v] = value
        
