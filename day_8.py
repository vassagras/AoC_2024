import time
import os

moves = {
    "u-l": (-1, -1),
    "d-r": (1, 1),
    "u-r": (-1, 1),
    "d-l": (1, -1)
}

def search_antinodes(start_pos, dif_x, dif_y, direction, x_limit, y_limit, nodes):
    """

    :param start_pos: current coordinates of the antenna
    :param dif_x: distance on the x-axis between two antennas of the same type
    :param dif_y: distance on the y-axis between two antennas of the same type
    :param direction: direction towards which the search of new anti-nodes is conducted
    :param x_limit: maximum number of rows
    :param y_limit: maximum number of columns
    :param nodes: list of anti-nodes identified so far
    :return:
    """
    move = moves[direction]
    cur_x = start_pos[0]
    cur_y = start_pos[1]
    while cur_x in range(0, x_limit) and cur_y in range(0, y_limit):
        nodes.add((cur_x, cur_y))
        next_x = cur_x + move[0] * abs(dif_x)
        next_y = cur_y + move[1] * abs(dif_y)
        if next_x in range(0, x_limit) and next_y in range(0, y_limit):
            #print("Add")
            nodes.add((next_x, next_y))
        cur_x, cur_y = next_x, next_y
    return

start = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 8"), 'r')

antennas = {}
x_len, y_len = 0, 0
# Read each line and store all the antenna's position creating a dictionary with the antenna types as keys and values
# the coordinates of the antennas
for i_index, line in enumerate(file):
    x_len = i_index
    for j_index, c in enumerate(line.replace('\n', '')):
        y_len = j_index
        if c == ".": continue
        if c not in antennas.keys():
            antennas[c] = [(i_index, j_index)]
        else:
            antennas[c].append((i_index, j_index))
x_len += 1
y_len += 1

antinodes = set()
for antenna_type in antennas.keys():
    for i, a in enumerate(antennas[antenna_type]):
        for _a in antennas[antenna_type][i+1:]:
            dx = a[0] - _a[0]
            dy = a[1] - _a[1]
            # dy > 0 indicates a positive slope for the line linking the two points
            if dy > 0:
                # Searching for a possible anti-node up-right
                if a[0] - abs(dx) in range(0, x_len) and a[1] + abs(dy) in range(0, y_len):
                    antinodes.add((a[0] - abs(dx), a[1] + abs(dy)))
                # Searching for a possible anti-node down-left
                if _a[0] + abs(dx) in range(0, x_len) and _a[1] - abs(dy) in range(0, y_len):
                    antinodes.add((_a[0] + abs(dx), _a[1] - abs(dy)))
            # dy < 0 indicates a negative slope for the line linking the two points
            else:
                # Searching for a possible anti-node up-left
                if a[0] - abs(dx) in range(0, x_len) and a[1] - abs(dy) in range(0, y_len):
                    antinodes.add((a[0] - abs(dx), a[1] - abs(dy)))
                # Searching for a possible anti-node down-right
                if _a[0] + abs(dx) in range(0, x_len) and _a[1] + abs(dy) in range(0, y_len):
                    antinodes.add((_a[0] + abs(dx), _a[1] + abs(dy)))

end = time.time()
print("Part 1 result: {}".format(len(antinodes)))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()

antinodes_2 = set()
for antenna in antennas.keys():
    for i, a in enumerate(antennas[antenna]):
        for _a in antennas[antenna][i + 1:]:
            dx = a[0] - _a[0]
            dy = a[1] - _a[1]

            if dy > 0:
                search_antinodes(a, dx, dy, "u-r", x_len, y_len, antinodes_2)
                search_antinodes(_a, dx, dy, "d-l", x_len, y_len, antinodes_2)
            else:
                search_antinodes(a, dx, dy, "u-l", x_len, y_len, antinodes_2)
                search_antinodes(_a, dx, dy, "d-r", x_len, y_len, antinodes_2)

end = time.time()
print("Part 2 result: {}".format(len(antinodes.union(antinodes_2))))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()
