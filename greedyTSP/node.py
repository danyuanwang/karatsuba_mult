class Node:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index
    def __str__(self):
        return str(self.index)

    def getX(self):
        return self.x

    def getY(self):
        return self.y