import time
import re
import os

def move_robot(pos, vel, max_x, max_y, seconds):
    """

    :param pos: starting position of the robot
    :param vel: velocity of the robot
    :param max_x: number of rows of the map / grid
    :param max_y: number of cols of the map / grid
    :param seconds: number of seconds to elapse
    :return: new position of the robot
    """
    cur_x = pos[0]
    cur_y = pos[1]
    new_x = (cur_x + vel[0] * seconds) % max_x
    new_y = (cur_y + vel[1] * seconds) % max_y
    return [new_x, new_y]

start = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 14"), 'r')

REGEX = r"^p=(\d*),(\d*) v=(-?\d*),(-?\d*)\n*"
MAX_X = 103 # 7 103
MAX_Y = 101 # 11 101
quadrant_1 = quadrant_2 = quadrant_3 = quadrant_4 = 0
QUADRANT_X = 51 #51 3
QUADRANT_Y = 50 #50 5

robots = []
robot_id = 0
for l in file:
    elements = re.findall(REGEX, l)
    # the input data first contain y-coordinate and then the x-coordinate
    start_pos = [int(elements[0][1]), int(elements[0][0])]
    move = (int(elements[0][3]), int(elements[0][2]))
    robots.append((robot_id, start_pos, move))
    robot_id += 1

for robot in robots:
    position = robot[1]
    velocity = robot[2]
    x, y = move_robot(position, velocity, MAX_X, MAX_Y, 100)
    robot[1][0] = x
    robot[1][1] = y
    if x < QUADRANT_X and y < QUADRANT_Y:
        quadrant_1 += 1
    elif x < QUADRANT_X and y > QUADRANT_Y:
        quadrant_2 += 1
    elif x > QUADRANT_X and y < QUADRANT_Y:
        quadrant_3 += 1
    elif x > QUADRANT_X and y > QUADRANT_Y:
        quadrant_4 += 1

safety_factor= quadrant_1 * quadrant_2 * quadrant_3 * quadrant_4

end = time.time()
print("Part 1 result: {}".format(safety_factor))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()
