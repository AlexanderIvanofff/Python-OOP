rows, cols = [int(x) for x in input().split()]

matrix = []

count = 0
for _ in range(rows):
    matrix.append([x for x in input().split()])

for row in range(rows - 1):
    for col in range(cols - 1):

        sum_matrix = []
        counter = 0

        for r in range(row, row + 2):
            sum_matrix.append([])

            for c in range(col, col + 2):
                sum_matrix[counter].append(matrix[r][c])

            counter += 1

        if sum_matrix[0] == sum_matrix[1] and sum_matrix[0][0] == sum_matrix[0][1]:
            count += 1

print(count)