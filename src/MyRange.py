# MyRange.py

class MyRange:
    def __init__(self, num_to_iterate):
        self.num_to_iterate = num_to_iterate
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.index >= self.num_to_iterate):
            raise StopIteration
        self.index += 1
        return self.index

