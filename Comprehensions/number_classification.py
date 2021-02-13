numbers = [int(x) for x in input().split(', ')]


def positive_number(number):
    result = [x for x in number if x >= 0]
    return f'Positive: {", ".join([str(x) for x in result])}'


def negative_number(number):
    result = [x for x in number if x < 0]
    return f'Negative: {", ".join([str(x) for x in result])}'


def even_number(number):
    result = [x for x in number if x % 2 == 0]
    return f'Even: {", ".join([str(x) for x in result])}'


def odd_number(number):
    result = [x for x in number if x % 2 != 0]
    return f'Odd: {", ".join([str(x) for x in result])}'


print(positive_number(numbers))
print(negative_number(numbers))
print(even_number(numbers))
print(odd_number(numbers))