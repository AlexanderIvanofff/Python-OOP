# You will receive a list of numbers. Separate the negative numbers from the positive. Find the total sum
# of the negatives and positives, replace the negative number with its absolute value and print the following:
# If the absolute negative number is bigger than the positive number:
# 	"The negatives are stronger than the positives"
# If the positive number is bigger than the absolute negative number:
# 	"The positives are stronger than the negatives"


def solve(numbers):
    positive_numbers = sum(filter(lambda x: x >= 0, numbers))
    negative_numbers = sum(filter(lambda x: x < 0, numbers))
    print(negative_numbers)
    print(positive_numbers)

    if positive_numbers > abs(negative_numbers):
        return f'The positives are stronger than the negatives'
    return f'The negatives are stronger than the positives'


input_numbers = list([int(x) for x in input().split()])
print(solve(input_numbers))