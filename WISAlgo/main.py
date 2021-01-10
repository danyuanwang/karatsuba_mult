from WIS import WIS
import sys
sys.setrecursionlimit(10000)
wis = WIS()
#print(wis.data)

print(bin(wis.testWIS(wis.findWIS(len(wis.data)-1))))

#print(wis.records)