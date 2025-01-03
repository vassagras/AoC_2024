import time
import os
from collections import Counter


def get_path(x1, y1, x2, y2, racetrack_map):
    """

    :param x1: the start x-coordinate
    :param y1: the start y-coordinate
    :param x2: the end x-coordinate
    :param y2: the end y-coordinate
    :param racetrack_map: the racetrack map
    :return:
    """
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = set()
    track = []
    x, y = x1, y1
    track.append((x, y))
    # there is only one path between the start and end points
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
    """

    :param point_1: point 1 from the path
    :param point_2: point 2 from the path
    :param track: the racetrack map
    :return: returns 2 if the manhattan distance between the two points is exactly 2, there is a wall between them, and
    the two points are in the same row or column.
    """
    # the two points must have a manhattan distance of 2 i.e., p1 - wall - p2
    if abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1]) == 2 :
        # the point between the two must be a wall and the two points must be in the same row or column
        point_3 = (int(point_1[0] + (point_2[0] - point_1[0]) / 2), int(point_1[1] + (point_2[1] - point_1[1]) / 2))
        if track[point_3[0]][point_3[1]] == "#" and (point_1[0] == point_2[0] or point_1[1] == point_2[1]):
            return 2
    return 0

def is_cheat_v2(point_1, point_2):
    # the two points must have a manhattan distance of 20
    if abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1]) <= 20 :
            return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])
    return 0

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
path_costs = {p:len(path) - i for i, p in enumerate(path)}

counter_part_1 = Counter()
for i in range(0, len(path)):
    p1 = path[i]
    for p2 in path[i+1:]:
        if is_cheat(p1, p2, racetrack) == 2:
            cheat_savings = abs(path_costs[p2] - path_costs[p1] + 2)
            counter_part_1.update([cheat_savings])
total_nbr_of_cheats = 0
for k, v in counter_part_1.items():
    # print("There are {} cheats that save {} picoseconds.".format(v, k))
    if k >= 100:
        total_nbr_of_cheats += v

end = time.time()
print("Part 1 result: {}".format(total_nbr_of_cheats))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()

start = time.time()
counter_part_2 = Counter()
for i in range(0, len(path)):
    p1 = path[i]
    for p2 in path[i+1:]:
        if is_cheat_v2(p1, p2) > 0:
            cheat_savings = abs(path_costs[p2] - path_costs[p1] + is_cheat_v2(p1, p2))
            counter_part_2.update([cheat_savings])
total_nbr_of_cheats = 0
for k, v in counter_part_2.items():
    # print("There are {} cheats that save {} picoseconds.".format(v, k))
    if k >= 100:
        total_nbr_of_cheats += v

end = time.time()
print("Part 2 result: {}".format(total_nbr_of_cheats))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()