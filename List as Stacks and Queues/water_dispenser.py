from collections import deque

quantity_liters = int(input())

people = deque()

while True:
    command = input()
    if command == 'Start':
        break
    else:
        name = command
        people.append(name)


while True:
    command = input()
    if command.isdigit():
        litters_to_drink = int(command)
        person = people.popleft()
        if litters_to_drink <= quantity_liters:
            quantity_liters -= litters_to_drink
            print(f'{person} got water')
        else:
            print(f'{person} must wait')
    elif command.startswith("refill "):
        liters_to_add = int(command.split(' ')[-1])
        quantity_liters += liters_to_add
    elif command == 'End':
        break

print(f'{quantity_liters} liters left')