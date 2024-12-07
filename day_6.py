import time
import os
from typing import List

start_p1 = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 6"), 'r')

#The directions rotate as follows: ^, >, <, v
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
start_x = 59
start_y = 62
visited = set()
grid: list[str] = []

for l in file:
    grid.append(l.rstrip())
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
        current_x -= _x
        current_y -= _y
        rotation_count += 1

end_p1 = time.time()
print("Part 1 result: {}".format(len(visited)))
print("The time of execution of above program is :", (end_p1 - start_p1) * 10**3, "ms")
print()