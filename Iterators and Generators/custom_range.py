class CustomRange:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.index = first

    def __iter__(self):
        self.index = self.first
        return self

    def __next__(self):
        if self.index > self.last:
            raise StopIteration
        index = self.index
        self.index += 1
        return index


cr = CustomRange(1, 4)
[print(x) for x in cr]
[print(x) for x in cr]
