n = int(input())

matrix = []
for _ in range(n):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)

print(sum([matrix[i][i] for i in range(len(matrix))]))