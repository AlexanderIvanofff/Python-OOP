def solve(command, list_of_numbers):
    if command == 'Even':
        even_numbers = sum(filter(lambda x: x % 2 == 0, list_of_numbers)) * len(list_of_numbers)
        return even_numbers
    elif command == 'Odd':
        odd_numbers = sum(filter(lambda x: x % 2 != 0, list_of_numbers)) * len(list_of_numbers)
        return odd_numbers


print(solve(input(), [int(x) for x in input().split()]))
