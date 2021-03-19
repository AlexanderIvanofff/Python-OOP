squares = lambda n: (i ** 2 for i in range(1, n + 1))

print(list(squares(5)))


def squares(n):
    for i in range(1, n + 1):
        yield i ** 2


def genrange(start, end):
    for i in range(start, end + 1):
        yield i


print(list(squares(5)))
print(list(genrange(1, 10)))
