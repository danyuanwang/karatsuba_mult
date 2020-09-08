class heap():
    def __init__(self, queue_size):
        self.q_size = queue_size
        self.q = [0] * (queue_size + 1)
        self.n = 0



    def parent(self, n):
        if n == 0: return -1
        if n == 1: return -1
        else: return int(n/2)

    def swap(self, i, j):
        t = self.q[j]
        self.q[j] = self.q[i]
        self.q[i] = t

    def young_child(self, index):
        return index * 2

    def length(self):
        return self.n