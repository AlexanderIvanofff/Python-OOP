n = int(input())

longest_intersection = set()
best_intersection = 0

for _ in range(n):
    ranges = input().split('-')
    first_range = ranges[0].split(',')
    first_range_start = int(first_range[0])
    first_range_end = int(first_range[1])
    first_set = set([x for x in range(first_range_start, first_range_end + 1)])

    second_range = ranges[1].split(',')
    second_range_start = int(second_range[0])
    second_range_end = int(second_range[1])
    second_set = set([x for x in range(second_range_start, second_range_end + 1)])

    intersection = first_set & second_set

    if len(intersection) > best_intersection:
        best_intersection = len(intersection)
        longest_intersection = intersection


print(f'Longest intersection is [{", ".join([str(x) for x in longest_intersection])}] with length '
      f'{len(longest_intersection)}')