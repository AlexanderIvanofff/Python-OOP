n = int(input())
cars = set()

for _ in range(n):
    (command, car) = input().split(', ')
    if command == 'IN':
        cars.add(car)
    else:
        cars.remove(car)

if cars:
    [print(car) for car in cars]
else:
    print(f'Parking Lot is Empty')