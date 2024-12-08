import time
import os

start_p1 = time.time()
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

end_p1 = time.time()
print("Part 1 result: {}".format(len(antinodes)))
print("The time of execution of above program is :", (end_p1 - start_p1) * 10**3, "ms")
print()
