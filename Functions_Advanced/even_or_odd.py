# Create a function called even_odd that can receive different amount of numbers and a command at the end.
# The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list.
# Submit only the function in the judge system.

def even_odd(*args):
    command = args[-1]

    if command == 'even':
        return list(filter(lambda x: x % 2 == 0, args[:-1]))
    elif command == 'odd':
        return list(filter(lambda x: x % 2 != 0, args[:-1]))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))