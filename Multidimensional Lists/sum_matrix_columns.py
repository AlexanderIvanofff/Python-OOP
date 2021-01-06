def read_int_from_list_input(separator):
    return [int(x) for x in input().split(separator)]


row_count, column_count = read_int_from_list_input(", ")

matrix = []

for _ in range(row_count):
    matrix.append(
        read_int_from_list_input(' ')
    )

sum_rows = [0] * column_count

for row in range(row_count):
    for column in range(column_count):
        sum_rows[column] += matrix[row][column]

[print(x) for x in sum_rows]