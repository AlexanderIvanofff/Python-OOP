def count_numbers(values):
    values_counts = {}

    for value in values:
        if value not in values_counts:
            values_counts[value] = 0
        values_counts[value] += 1

    return values_counts


def print_result(values_counts):
    for (value, count) in values_counts.items():
        print(f'{value} - {count} times')


print_result(count_numbers(map(float, input().split(' '))))