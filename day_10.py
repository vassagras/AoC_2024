import time
import os

def find_walk_trail(_x:int, _y:int, _m:list, _p: set):
    """

    :param _x: x coordinate
    :param _y: y coordinate
    :param _m: topographic map
    :param _p: set of all the final positions of a valid trailhead
    :return:
    """
    curr_height = _m[_x][_y]
    if curr_height == 9:
        _p.add((_x, _y))
        return
    # check up
    if _x > 0 and _m[_x - 1][_y] == curr_height + 1:
        find_walk_trail(_x-1, _y, _m, _p)
    # check down
    if _x < len(_m) - 1 and _m[_x + 1][_y] == curr_height + 1:
        find_walk_trail(_x+1, _y, _m, _p)
    # check left
    if _y > 0 and _m[_x][_y - 1] == curr_height + 1:
        find_walk_trail(_x, _y-1, _m, _p)
    # check right
    if _y < len(_m[_x]) - 1 and _m[_x][_y + 1] == curr_height + 1:
        find_walk_trail(_x, _y + 1, _m, _p)

    return


def count_walk_trail(_x:int, _y:int, _m:list):
    curr_height = _m[_x][_y]
    cnt = 0
    if curr_height == 9:
        return 1
    # check up
    if _x > 0 and _m[_x - 1][_y] == curr_height + 1:
        cnt += count_walk_trail(_x-1, _y, _m)
    # check down
    if _x < len(_m) - 1 and _m[_x + 1][_y] == curr_height + 1:
        cnt += count_walk_trail(_x+1, _y, _m)
    # check left
    if _y > 0 and _m[_x][_y - 1] == curr_height + 1:
        cnt += count_walk_trail(_x, _y-1, _m)
    # check right
    if _y < len(_m[_x]) - 1 and _m[_x][_y + 1] == curr_height + 1:
        cnt += count_walk_trail(_x, _y + 1, _m)

    return cnt

start = time.time()
matrix = []
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 10"), 'r')
for l in file:
    matrix.append([int(i) for i in list(l.replace("\n", ""))])

counter = 0
trailheads = []
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        if matrix[i][j] == 0:
            trailheads.append((i, j))

counter = 0
for th in trailheads:
    final_pos = set()
    find_walk_trail(th[0], th[1], matrix, final_pos)
    counter += len(final_pos)

end = time.time()
print("Part 1 result: {}".format(counter))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()

start = time.time()
counter = 0
for th in trailheads:
    counter += count_walk_trail(th[0], th[1], matrix)

end = time.time()
print("Part 2 result: {}".format(counter))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()
