import time
import os
from collections import Counter


def get_path(x1, y1, x2, y2, racetrack_map):
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = set()
    track = []
    x, y = x1, y1
    track.append((x, y))
    while x != x2 or y != y2:
        for _x, _y in [(x+dx, y+dy) for (dx, dy) in moves]:
            if (racetrack_map[_x][_y] == "." or racetrack_map[_x][_y] == "E") and (_x, _y) not in visited:
                track.append((_x, _y))
                visited.add((_x, _y))
                x = _x
                y = _y
                break
    return track

def is_cheat(point_1, point_2, track):
    if abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1]) == 2 :
        point_3 = (int(point_1[0] + (point_2[0] - point_1[0]) / 2), int(point_1[1] + (point_2[1] - point_1[1]) / 2))
        if track[point_3[0]][point_3[1]] == "#" and (point_1[0] == point_2[0] or point_1[1] == point_2[1]):
            return True
    return False

start = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 20"), 'r')
racetrack = []
for line in file:
    racetrack.append(list(line.replace("\n", "")))

source_x = 79 # 3
source_y = 59 # 1
end_x = 87 # 7
end_y = 39 # 5
path = get_path(source_x, source_y, end_x, end_y, racetrack)
cost_of_path = len(path)
path_costs = {p:cost_of_path - i for i, p in enumerate(path)}

nbr_of_cheats = 0
c = Counter()
for i in range(0, len(path)):
    p1 = path[i]
    for p2 in path[i+1:]:
        if is_cheat(p1, p2, racetrack):
            nbr_of_cheats += 1
            cheat_savings = abs(path_costs[p2] - path_costs[p1] + 2)
            c.update([cheat_savings])
total = 0
for k, v in c.items():
    print("There are {} cheats that save {} picoseconds.".format(v, k))
    if k >= 100:
        total += v
print()

end = time.time()
print("Part 1 result: {}".format(total))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()