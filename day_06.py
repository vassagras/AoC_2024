import copy
import time
import os
from typing import List

start = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 06"), 'r')

#The directions rotate as follows: ^, >, v, <
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
directions = ["^", ">", "v", "<"]
start_x = 6 # 59 # 6
start_y = 4 # 62 # 4
visited = set()
grid = []

for l in file:
    grid.append(list(l.rstrip()))
len_x, len_y = len(grid), len(grid[0])

current_x, current_y = start_x, start_y
rotation_count = 0
while current_x in range(0, len_x) and current_y in range(0, len_y):
    _x, _y = moves[rotation_count % 4]
    if grid[current_x][current_y] != "#":
        visited.add((current_x, current_y))
        current_x += _x
        current_y += _y
    else:
        rotation_count += 1
        current_x -= _x
        current_y -= _y

end = time.time()
print("Part 1 result: {}".format(len(visited)))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()

start = time.time()

# We iterate over all visited positions and check whether there will be a loop in case we place an obstacle
number_of_potential_loops = 0
for potential_obstacle in visited:
    # Place a temp obstacle at the current visited position
    obstacle_x, obstacle_y = potential_obstacle
    grid[obstacle_x][obstacle_y] = "#"

    # Go back to the original starting coordinates and re-run part 1's logic
    current_x, current_y = start_x, start_y
    rotation_count = 0
    temp_visited = set()

    while current_x in range(0, len_x) and current_y in range(0, len_y):
        # If we go bock to the same position, then it is a loop
        if (current_x, current_y) in temp_visited:
            number_of_potential_loops += 1
            grid[obstacle_x][obstacle_y] = "."
            break
        _x, _y = moves[rotation_count % 4]
        if grid[current_x][current_y] != "#":
            temp_visited.add((current_x, current_y))
            current_x += _x
            current_y += _y
        else:
            rotation_count += 1
            current_x -= _x
            current_y -= _y
        grid[obstacle_x][obstacle_y] = "."

end = time.time()
print("Part 2 result: {}".format(number_of_potential_loops))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()
