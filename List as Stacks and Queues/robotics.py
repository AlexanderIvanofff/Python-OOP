"""
Somewhere in the future, there is a robotics factory. The current project is assembly line robots.
Each robot has a processing time, the time it needs to process a product.
When a robot is free it should take a product for processing and log his name, product and processing start time.
Each robot processes a product coming from the assembly line. A product is coming from the line each second
(so the first product should appear at [start time + 1 second]). If a product passes the line and there is not a
free robot to take it, it should be queued at the end of the line again.
The robots are standing on the line in the order of their appearance.

"""

from collections import deque


def next_second(h, m, s):
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        h = 0
    return h, m, s


robot_info = input().split(';')
robot_dict = {}
available_robots = deque()
waiting_robots = deque()
products = deque()

time = list(map(int, input().split(':')))

product = input()
while not product == 'End':
    products.append(product)
    product = input()

for robot in robot_info:
    robot_name = robot.split('-')[0]
    robot_time = int(robot.split('-')[1])
    available_robots.append([robot_name, robot_time])
    robot_dict[robot_name] = robot_time


while products:
    for robot in waiting_robots:
        robot_name = robot[0]
        robot[1] -= 1
        if robot[1] <= 0:
            available_robots.append([robot_name, robot_dict[robot_name]])
    waiting_robots = [r for r in waiting_robots if r[1] > 0]

    time = next_second(time[0], time[1], time[2])
    current_products = products.popleft()

    if not available_robots:
        products.append(current_products)
        continue

    current_robot = available_robots.popleft()
    print(f'{current_robot[0]} - {current_products} [{time[0]:02d}:{time[1]:02d}:{time[2]:02d}]')
    waiting_robots.append(current_robot)