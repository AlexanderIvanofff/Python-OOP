# Write a function called list_manipulator which receives a list of numbers as first parameter and different amount of
# other parameters. The second parameter might be "add" or "remove". The third parameter might be "beginning" or "end".
# There might or might not be any other parameters (numbers):
# •	In case of "add" and "beginning", add the given numbers to the beginning of the given list of numbers and
# return the new list
# •	In case of "add" and "end", add the given numbers to the end of the given list of numbers and return the new list
# •	In case of "remove" and "beginning"
# o	If there is another parameter (number), remove that amount of numbers from the beginning of the list of numbers.
# o	If there are no other parameters, remove only the first element of the list.
# o	Finaly, return the new list
# •	In case of "remove" and "end"
# o	If there is another parameter (number), remove that amount of numbers from the end of the list of numbers.
# o	Otherwise if there are no other parameters, remove only the last element of the list.
# o	Finaly, return the new list
# For more clarifications, see the examples below.


from collections import deque


def list_manipulator(current_lst, operation, position, *args):
    new_list = deque(current_lst)

    if operation == 'add':
        if position == 'beginning':
            if len(args) > 0:
                new_list = deque(args) + new_list

        elif position == 'end':
            if len(args) > 0:
                new_list += deque(args)

    elif operation == 'remove':
        if position == 'beginning':
            if 0 <= len(args) <= 1:
                n = args[0] if len(args) == 1 else 1
                fn = new_list.popleft if position == 'beginning' else new_list.pop
                for _ in range(n):
                    fn()

        elif position == 'end':
            if 0 <= len(args) <= 1:
                n = args[0] if len(args) == 1 else 1
                fn = new_list.popleft if position == 'beginning' else new_list.pop
                for _ in range(n):
                    fn()

    return list(new_list)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
