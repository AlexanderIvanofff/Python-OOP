def sub_expression(expression):
    s = []
    result = []
    for index in range(len(expression)):
        char = expression[index]
        if char == '(':
            s.append(index)
        elif char == ')':
            start_index = s.pop()
            result.append(expression[start_index:index + 1])
    return result


for ch in sub_expression(input()):
    print(ch)