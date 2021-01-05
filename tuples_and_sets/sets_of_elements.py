tokens = list(map(int, input().split(' ')))

n_length = tokens[0]
m_length = tokens[1]


n = set()
m = set()

[n.add(input()) for _ in range(n_length)]
[m.add(input()) for _ in range(m_length)]


intersection = n.intersection(m)

[print(number) for number in intersection]