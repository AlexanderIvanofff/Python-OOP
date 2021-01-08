def sum_primary_diagonal(matrix):
    return sum([matrix[i][i] for i in range(len(matrix))])


def sum_secondary_diagonal(matrix):
    return sum([matrix[i][-i - 1] for i in range(len(matrix))])


def different_sum_secondary_dig_and_primary_dig(matrix):
    print(abs(sum_primary_diagonal(matrix) - sum_secondary_diagonal(matrix)))


n = int(input())

current_matrix = []

for _ in range(n):
    current_matrix.append([int(x) for x in input().split()])


different_sum_secondary_dig_and_primary_dig(current_matrix)