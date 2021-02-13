n = int(input())

elements = set()

for _ in range(n):
    tokens = set(input().split(' '))
    elements = elements.union(tokens)


[print(element) for element in elements]