class hash_table():
    def __init__(self):
        self.dict = {}

    def insert(self, key):
        self.dict[key] = 1

    def delete(self, key):
        self.dict.pop(key)

    def look_up(self, key):
        if key in self.dict.keys():
            return self.dict[key]
        return 0
