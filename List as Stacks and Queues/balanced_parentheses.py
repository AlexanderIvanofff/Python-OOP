parentheses = input()
is_balanced = True

opening = []
mirror = {'{': '}', '[': ']', '(': ')'}

for char in parentheses:
    if char in '{[(':
        opening.append(char)
    else:
        if not opening:
            is_balanced = False
            break
        current_opening_p = opening.pop()
        if not mirror[current_opening_p] == char:
            is_balanced = False
            break

if is_balanced:
    print('YES')
else:
    print('NO')
