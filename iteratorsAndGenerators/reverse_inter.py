class reverse_iter:
    def __init__(self, iterator):
        self.iterator = iterator
        self.index = len(iterator)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index >= 0:
            return self.iterator[self.index]
        raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
