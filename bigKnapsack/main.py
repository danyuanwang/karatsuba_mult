from knapsack import Knapsack
import time
import sys
sys.setrecursionlimit(10000)
knapsack = Knapsack()
startTime = time.time()
result = knapsack.findOptimum(knapsack.itemCount, knapsack.knapCapacity)
print(time.strftime("%H:%M:%S", time.gmtime(time.time()-startTime)))
print(result)