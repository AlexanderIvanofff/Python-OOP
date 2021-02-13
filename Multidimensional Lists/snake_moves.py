from collections import deque

rows, column = [int(x) for x in input().split()]
snake = deque(input())

for row in range(rows):
    s = ''
    for col in range(column):
        piece = snake.popleft()
        s += piece
        snake.append(piece)
    if row % 2 == 0:
        print(s)
    else:
        print(s[::-1])