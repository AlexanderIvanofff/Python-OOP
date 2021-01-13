"""
Our favorite super-spy action hero Sam is back from his mission in the previous exam, and he has finally found some time
to go on a holiday. He is taking his wife somewhere nice and they're going to have a really good time, but first, they
have to get there. Even on his holiday trip, Sam is still going to run into some problems and the first one is, of course,
getting to the airport. Right now, he is stuck in a traffic jam at a very active crossroads where a lot of accidents happen.
Your job is to keep track of traffic at the crossroads and report whether a crash happened or everyone passed the crossroads
safely and our hero is one step closer to a much desired vacation.
The road Sam is on has a single lane where cars queue up until the light goes green. When it does, they start passing
one by one during the green light and the free window before the intersecting road's light goes green. During one second
only one part of a car (a single character) passes the crossroads. If a car is still in the crossroads when the free
window ends, it will get hit at the first character that is still in the crossroads.
"""


from collections import deque

green_light = int(input())
window_light = int(input())
crashed = False
cars = deque()
all_cars = []

line = input()
while not line == 'END':
    if line == 'green':
        timer = green_light
        if cars:
            cars_copy = cars.popleft()
            current_car = deque(cars_copy)

            while timer:
                if not current_car:
                    if cars:
                        cars_copy = cars.popleft()
                        current_car = deque(cars_copy)
                    else:
                        break
                current_car.popleft()
                timer -= 1
            if current_car:
                window_timer = window_light
                while window_timer and current_car:
                    current_car.popleft()
                    window_timer -= 1
            if current_car:
                crashed = True
                print(f'A crash happened!')
                print(f'{cars_copy} was hit at {current_car.popleft()}.')
                break
    else:
        cars.append(line)
        all_cars.append(line)
    line = input()

if not crashed:
    left_cars = abs(len(cars) - len(all_cars))
    print(f'Everyone is safe.')
    print(f'{left_cars} total cars passed the crossroads.')