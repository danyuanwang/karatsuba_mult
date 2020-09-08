from heap_class import heap


class heap_max(heap):
    def __init__(self, queue_size):
        super().__init__(queue_size)

    def insert(self, key):
        if self.n >= self.q_size:
            print('warning')
        else:
            self.n += 1
            self.q[self.n] = key
            self.bubble_up(key)
        

    def extract_root(self):
        min_val = -1
        if(self.n <= 0):
            print('empty queue')
        else:
            min_val = self.q[1]
            self.q[1] = self.q[self.n]
            self.n -= 1
            self.bubble_down(1)
        return min_val

    def bubble_up(self, index):
        if self.parent(index) == -1:
            return
        if self.q[self.parent(index)] < self.q[index]:
            self.swap(index, self.parent(index))
            self.bubble_up(self.parent(index))


    def bubble_down(self, index):

        c = self.young_child(index)
        min_index = index
        
        for i in range(2):
            if (c + i) <= self.n:
                if ( self.q[min_index] < self.q[c + i]):
                    min_index =  c + i

        if min_index != index :
            self.swap(index, min_index)
            self.bubble_down(min_index)