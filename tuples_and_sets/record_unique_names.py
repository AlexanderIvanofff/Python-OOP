n = int(input())
names = set()

[names.add(input()) for _ in range(n)]
[print(name) for name in names]