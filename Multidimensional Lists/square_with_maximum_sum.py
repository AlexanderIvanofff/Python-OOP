def read_int_from_list_input(separator):
    return [int(x) for x in input().split(separator)]


row_count, column_count = read_int_from_list_input(", ")

matrix = []
for _ in range(row_count):
    matrix.append(read_int_from_list_input(", "))


def get_submatrix_sum(matrix, row, col):
    return matrix[row][col] + matrix[row][col + 1] + \
           matrix[row + 1][col] + matrix[row + 1][col + 1]


def print_sum_matrix(matrix, row, col):
    for r in range(row, row + 2):
        for c in range(col, col + 2):
            print(matrix[r][c], end=' ')
        print()


best_position = (0, 0)
best_value = get_submatrix_sum(matrix, 0, 0)

for row in range(len(matrix) -1):
    for col in range(len(matrix[row]) - 1):
        current_value = get_submatrix_sum(matrix, row, col)
        if best_value < current_value:
            best_value = current_value
            best_position = (row, col)


(best_row, best_col) = best_position
print_sum_matrix(matrix, best_row, best_col)
print(best_value)