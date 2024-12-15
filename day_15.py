import time
import os

def get_move_diff(move_direction):
    """

    :param move_direction: direction of the move i.e., <>v^
    :return: return the dx and dy based on the direction
    """
    if move_direction == "^":
        return -1, 0
    elif move_direction == "v":
        return 1, 0
    elif move_direction == "<":
        return 0, -1
    elif move_direction == ">":
        return 0, 1
    return 0, 0

def move_robot(x, y, move_direction, wh_map):
    """

    :param x: current x-coordinate of the robot
    :param y: current y-coordinate of the robot
    :param move_direction: direction of the move i.e., <>v^
    :param wh_map: warehouse map in form of a 2D array
    :return: the coordinates of the robot after considering the current move
    """
    dx, dy = get_move_diff(move_direction)
    new_x = x + dx
    new_y = y + dy

    # If the robot hits a wall, then there is no change in its position
    if wh_map[new_x][new_y] == "#":
        return x, y
    # if there is a free space towards the direction of the robot's move, then the robot changes to it
    elif wh_map[new_x][new_y] == ".":
        wh_map[new_x][new_y] = "@"
        wh_map[x][y] = "."
        return new_x, new_y
    # if there is a box, then the robot attempts to push it
    elif wh_map[new_x][new_y] == "O":
        # counter keeps track of how many positions we look ahead
        counter = 1
        _new_x, _new_y = new_x, new_y

        # keep looking ahead while there are boxes
        while wh_map[_new_x][_new_y] == "O":
            _new_x = _new_x + dx
            _new_y = _new_y + dy
            counter += 1

        # check if the next position after the last box is a free space (.) or a wall
        if wh_map[_new_x][_new_y] == ".":
            wh_map[new_x][new_y] = "@"
            wh_map[x][y] = "."
            for k in range(1, counter):
                wh_map[new_x + k*dx][new_y + k*dy] = "O"
            return new_x, new_y
        else:
            return x, y

start = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 15"), 'r')
file_moves = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 15 moves"), 'r')

warehouse_map = []
for line in file:
    warehouse_map.append(list(line.replace("\n", "")))
moves = file_moves.read().replace("\n", "")

#print("Initial state:")
#for row in warehouse_map:
#    print("".join(row))
#print()

# Initial values are the coordinates of the robot
current_x = 24
current_y = 24
for direction in moves:
    #print("Move {}:".format(direction))
    current_x, current_y = move_robot(current_x, current_y, direction, warehouse_map)
    #for row in warehouse_map:
    #    print("".join(row))
    #print()

gps_distance = 0
for i in range(0, len(warehouse_map)):
    for j in range(0, len(warehouse_map[0])):
        if warehouse_map[i][j] == "O":
            gps_distance += 100 * i + j

end = time.time()
print("Part 1 result: {}".format(gps_distance))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()