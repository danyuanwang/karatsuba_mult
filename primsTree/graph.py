from edgeData import EdgeData


class Group():
    def __init__(self):
        self.list = []

    def add(self, node):
        self.list.append(node)
        self.list = list(set(self.list))


    
    def remove(self, node):
        for i in self.list:
            if i == node:
                self.list.remove(i)

    def size(self):
        return len(self.list)
