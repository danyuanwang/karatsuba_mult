import math
from node import Node
class Data:
    def __init__(self, link):
        self.size = 0
        self.graph = []
        # handle = open('test_data.txt')
        handle = open(link)
        for line in handle:
            a = line.split()
            print(a)
            node = Node(float(a[0]), float(a[1]), self.size)
            self.graph.append(node)
            self.size += 1

    def dist(self, a, b):
        dist = math.sqrt((a.x- b.x)**2 + (a.y- b.y)**2)
        return dist