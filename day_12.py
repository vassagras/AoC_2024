import time
import os

def identify_area(plant_type, x, y, plot, area):
    """

    :param plant_type: Type of plant
    :param x: x-coordinate
    :param y: y-coordinate
    :param plot: plot map / matrix
    :param area: array containing the shape coordinates
    :return:
    """
    if x < 0 or x >= len(plot) or y < 0 or y >= len(plot[0]):
        return
    else:
        if plot[x][y] == plant_type:
            area.append((x, y))
            if (x + 1, y) not in area:
                identify_area(plant_type, x + 1, y, plot, area)
            if (x - 1, y) not in area:
                identify_area(plant_type, x - 1, y, plot, area)
            if (x, y + 1) not in area:
                identify_area(plant_type, x, y + 1, plot, area)
            if (x, y - 1) not in area:
                identify_area(plant_type, x, y - 1, plot, area)
            return
        else:
            return

def identify_perimeter(area):
    """

    :param area: list of coordinates belonging to the area of the shape
    :return: returns the perimeter of the shape
    """
    per = 0
    for p in area:
        x, y = p
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        per += 4 - len(set(neighbors).intersection(set(area)))
    return per

start = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 12"), 'r')
plot_map = []
for l in file:
    plot_map.append(list(l.replace("\n", "")))

for row in plot_map:
    print("".join(row))
print()

total_price = 0
visited = set()
for i in range(0, len(plot_map)):
    for j in range(0, len(plot_map[0])):
        if (i, j) not in visited:
            shape_area = []
            identify_area(plot_map[i][j], i, j, plot_map, shape_area)
            visited.update(shape_area)
            shape_perimeter = identify_perimeter(shape_area)
            total_price += shape_perimeter * len(shape_area)
            print("A region of {} plants with area: {} and perimeter: {}".format(plot_map[i][j], len(shape_area), shape_perimeter))
print()

end = time.time()
print("Part 1 result: {}".format(total_price))
print("The time of execution of above program is :", (end - start) * 10**3, "ms")
print()
