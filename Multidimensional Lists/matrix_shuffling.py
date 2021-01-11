def is_valid(pos, rows, cols):
    return 0 <= pos[0] < rows and 0 <= pos[1] < cols


rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])


line = input().split()

while not line[0] == 'END':
    if line[0] == 'swap' and len(line) == 5:
        first_position = [int(line[1]), int(line[2])]
        second_position = [int(line[3]), int(line[4])]

        if is_valid(first_position, rows, cols) and is_valid(second_position, rows, cols):
            matrix[first_position[0]][first_position[1]], matrix[second_position[0]][second_position[1]] = \
                matrix[second_position[0]][second_position[1]], matrix[first_position[0]][first_position[1]]
            for row in matrix:
                print(' '.join(row))
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
    line = input().split()