import time
import os

start = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 8"), 'r')

antennas = {}
x_len, y_len = 0, 0
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

start = time.time()
antinodes_2 = set()
for t_antenna in antennas.keys():
    for i, a in enumerate(antennas[t_antenna]):
        for _a in antennas[t_antenna][i+1:]:
            dx = a[0] - _a[0]
            dy = a[1] - _a[1]

            # dy > 0 indicates a positive slope for the line linking the two points
            if dy > 0:
                # Searching for a possible anti-node up-right
                antinodes_2.add((a[0], a[1]))
                current_x = a[0]
                current_y = a[1]
                new_x = a[0] - abs(dx)
                new_y = a[1] + abs(dy)
                while current_x in range(0, x_len) and current_y in range(0, y_len):
                    if new_x in range(0, x_len) and new_y in range(0, y_len):
                        antinodes_2.add((new_x, new_y))
                    current_x = new_x
                    current_y = new_y
                    new_x -= abs(dx)
                    new_y += abs(dy)

                # Searching for a possible anti-node down-left
                antinodes_2.add((_a[0], _a[1]))
                current_x = _a[0]
                current_y = _a[1]
                new_x = _a[0] + abs(dx)
                new_y = _a[1] - abs(dy)
                while current_x in range(0, x_len) and current_y in range(0, y_len):
                    if new_x in range(0, x_len) and new_y in range(0, y_len):
                        antinodes_2.add((new_x, new_y))
                    current_x = new_x
                    current_y = new_y
                    new_x += abs(dx)
                    new_y -= abs(dy)

            # dy < 0 indicates a negative slope for the line linking the two points
            else:
                # Searching for a possible anti-node up-left
                antinodes_2.add((a[0], a[1]))
                current_x = a[0]
                current_y = a[1]
                new_x = a[0] - abs(dx)
                new_y = a[1] - abs(dy)
                while current_x in range(0, x_len) and current_y in range(0, y_len):
                    #print("Going up-left")
                    if new_x in range(0, x_len) and new_y in range(0, y_len):
                        antinodes_2.add((new_x, new_y))
                    current_x = new_x
                    current_y = new_y
                    new_x -= abs(dx)
                    new_y -= abs(dy)

                # Searching for a possible anti-node down-right
                antinodes_2.add((_a[0], _a[1]))
                current_x = _a[0]
                current_y = _a[1]
                new_x = _a[0] + abs(dx)
                new_y = _a[1] + abs(dy)
                while current_x in range(0, x_len) and current_y in range(0, y_len):
                    if new_x in range(0, x_len) and new_y in range(0, y_len):
                        antinodes_2.add((new_x, new_y))
                    current_x = new_x
                    current_y = new_y
                    new_x += abs(dx)
                    new_y += abs(dy)

end = time.time()
print("Part 2 result: {}".format(len(antinodes.union(antinodes_2))))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()
