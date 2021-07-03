import random
class Values:
    def __init__(self, cases):
        self.values = {}
        self. n = 0
        for case in cases.cases:
            for value in case:
                self.values[abs(value)] = random.choice([True, False])
            self.n += 1
        
    def generate(self):
        for value in self.values:
            self.values[abs(value)] = random.choice([True, False])
    def flip(self, index):
        self.values[abs(index)] = not self.values[abs(index)]


