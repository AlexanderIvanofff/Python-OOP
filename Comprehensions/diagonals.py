n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(', ')])

first_diagonal = [matrix[i][i] for i in range(len(matrix))]
second_diagonal = [matrix[i][-i -1] for i in range(len(matrix))]

first_diagonal_sum = sum([matrix[i][i] for i in range(len(matrix))])
second_diagonal_sum = sum([matrix[i][-i - 1] for i in range(len(matrix))])


print(f'First diagonal: {", ".join([str(x) for x in first_diagonal])}. Sum: {first_diagonal_sum}')
print(f'Second diagonal: {", ".join([str(x) for x in second_diagonal])}. Sum: {second_diagonal_sum}')
