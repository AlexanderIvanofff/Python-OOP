clothes = [int(x) for x in input().split()]
capacity = int(input())

current_capacity = 0
rack = 0

while len(clothes) > 0:
    while current_capacity <= capacity:
        index = len(clothes) - 1
        current_capacity += clothes[index]

        if current_capacity <= capacity:
            clothes.pop()
            if index == 0:
                rack += 1
                break
            if current_capacity == capacity:
                current_capacity = 0
                rack += 1
        else:
            current_capacity = 0
            rack += 1
            if index == 0:
                rack += 1
                clothes.pop()
                break
            continue

print(rack)