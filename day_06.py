import time
import os

#The directions rotate as follows: ^, >, v, <
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def discover_path(x, y, lab_grid, p2 = False):
    """

    :param x: x grid coordinate of the starting position
    :param y: y grid coordinate of the starting position
    :param lab_grid: the lab grid as a 2D matrix
    :return: returns the visited positions
    """
    length_x, length_y = len(lab_grid), len(lab_grid[0])

    cur_x, cur_y = x, y
    visited_positions = set()
    nbr_of_rotations = 0
    while cur_x in range(0, length_x) and cur_y in range(0, length_y):
        next_x, next_y = moves[nbr_of_rotations % 4]
        # while no obstacle is faced, then keep moving in the same direction
        if lab_grid[cur_x][cur_y] != "#":
            if p2:
                visited_positions.add((cur_x, cur_y, nbr_of_rotations % 4))
            else:
                visited_positions.add((cur_x, cur_y))
            cur_x += next_x
            cur_y += next_y
        # if an obstacle is encountered, then rotate by 90 degrees and get back to the previous position
        else:
            nbr_of_rotations += 1
            cur_x -= next_x
            cur_y -= next_y
    return visited_positions

start = time.time()

file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 06"), 'r')

start_x = 59 # 59 # 6
start_y = 62 # 62 # 4

grid = []
for l in file:
    grid.append(list(l.rstrip()))

visited = discover_path(start_x, start_y, grid)

end = time.time()
print("Part 1 result: {}".format(len(visited)))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()

start = time.time()

# Iterate over all visited positions and check whether there will be a loop in case an obstacle is placed
number_of_potential_loops = 0
for potential_obstacle in visited:
    # Place a temp obstacle at the current visited position
    obstacle_x, obstacle_y = potential_obstacle
    grid[obstacle_x][obstacle_y] = "#"

    # Go back to the original starting coordinates and re-run part 1's logic
    current_x, current_y = start_x, start_y
    rotation_count = 0
    current_visited = set()

    while current_x in range(0, len(grid)) and current_y in range(0, len(grid[0])):
        # If we go bock to the same position, then it is a loop
        if (current_x, current_y, rotation_count % 4) in current_visited:
            number_of_potential_loops += 1
            grid[obstacle_x][obstacle_y] = "."
            break
        _x, _y = moves[rotation_count % 4]
        if grid[current_x][current_y] != "#":
            current_visited.add((current_x, current_y, rotation_count % 4))
            current_x += _x
            current_y += _y
        else:
            rotation_count += 1
            current_x -= _x
            current_y -= _y
            if len(current_visited) > 0:
                current_visited.pop()
    grid[obstacle_x][obstacle_y] = "."

end = time.time()
print("Part 2 result: {}".format(number_of_potential_loops))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()
