import random
class Values:
    def __init__(self, n):
        self.n = n
        self.values = [False] * n
        
    def generate(self):
        for i in range(self.n):
            self.values[i] = random.choice([True, False])
    def flip(self, index):
        self.values[index] = not self.values[index]


