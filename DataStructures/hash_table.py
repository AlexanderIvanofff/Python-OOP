# Liner approach implementation of hashing


class HashTable:
    """
    Hashable representation a custom dictionary implementation
    where we use two private lists to achieve storing and hashing of
    key-value pairs functionality
    """

    def __init__(self):
        self.max_capacity = 8
        self.__keys = [None] * self.max_capacity
        self.__values = [None] * self.max_capacity

    def __getitem__(self, key):
        index = self.__keys.index(key)
        return self.__values[index]

    def resize(self):
        self.__keys = self.__keys + [None] * self.max_capacity
        self.__values = self.__values + [None] * self.max_capacity
        self.max_capacity = self.max_capacity * 2

    def __setitem__(self, key, value):
        if key in self.__keys:
            index = self.__keys.index(key)
            self.__values[index] = value
            return
        if self.length == self.max_capacity:
            self.resize()
        index = self.hash(key)
        self.__keys[index] = key
        self.__values[index] = value

    def get(self, key):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            return None

    def add(self, key, value):
        self[key] = value

    def check_available_index(self, index):
        if index == len(self.__keys):
            return self.check_available_index(0)
        if self.__keys[index] is None:
            return index
        return self.check_available_index(index + 1)

    def hash(self, key):
        index = sum([ord(char) for char in key]) % self.max_capacity
        available_index = self.check_available_index(index)
        return available_index

    def __len__(self):
        return self.max_capacity

    @property
    def length(self):
        return len([el for el in self.__keys if el is not None])

    def __repr__(self):
        result = [
            f"{self.__keys[index]}: {self.__values[index]}"
            for index in range(len(self.__keys))
            if self.__keys[index] is not None
        ]

        return "{" + "{}".format(", ".join(result)) + "}"


hash_table = HashTable()

hash_table["name"] = "Peter"
hash_table["age"] = 25
hash_table["color"] = "blue"
hash_table["animal"] = "Dog"
hash_table["course"] = "Python"

print(hash_table["name"])
print(hash_table.get(5))
print(hash_table["age"])
print(hash_table.length)
print(hash_table)
