string = input()

stack = []
for char in string:
    stack.append(char)

reversed_str = ""

while len(stack) > 0:
    item = stack.pop()
    reversed_str += item

print(reversed_str)