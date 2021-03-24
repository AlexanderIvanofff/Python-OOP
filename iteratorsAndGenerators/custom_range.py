class custom_range:
    def __init__(self, start, end):
        self.index = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        index = self.index
        if index <= self.end:
            self.index += 1
            return index
        raise StopIteration()


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
