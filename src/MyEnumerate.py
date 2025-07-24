# MyEnumerate.py

class MyEnumerate:
    def __init__(self, data, first_index=0):
        self.data = data
        self.index = 0
        self.first_index = first_index

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self, self.data[self.index])
        self.index += 1
        return value
