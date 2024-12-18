import time
import os

MAX_X = 71
MAX_Y = 71

def get_adjacent_vertices(cur_node, obstacles, visited_nodes, node_distances):
    cur_x, cur_y = cur_node
    cur_distance = node_distances[cur_node]
    neighbor_nodes = [(cur_x + 1, cur_y), (cur_x - 1, cur_y), (cur_x, cur_y + 1), (cur_x, cur_y - 1)]

    for n in neighbor_nodes:
        if n[0] < 0 or n[0] >= MAX_X or n[1] < 0 or n[1] >= MAX_Y:
            continue
        # Check that the space is not corrupted and that the node has not already been visited
        if n not in obstacles and n not in visited_nodes:
            if n not in node_distances:
                node_distances[n] = cur_distance + 1
            elif node_distances[n] > (cur_distance + 1):
                node_distances[n] = cur_distance + 1
    return None

start = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 18"), 'r')

# Initialize the memory space based on the input data
memory_space = []
corrupted_spaces = []
for l in file:
    y, x = [int(e) for e in l.replace("\n", "").split(",")]
    corrupted_spaces.append((x, y))
for i in range(0, MAX_X):
    row = []
    for j in range(0, MAX_Y):
        if (i, j) in corrupted_spaces:
            row.append("#")
        else:
            row.append(".")
    memory_space.append(row)
#for row in memory_space:
#    print("".join(row))

# Dijkstra's algorithm implementation to find the shortest path from the source to the destination node.
distances = {} # keeps track of the distances to the unvisited nodes
shortest_path = {} # keeps track of all the distances of the visited nodes

source_x, source_y = 0, 0
destination_x, destination_y = 70, 70
distances[(source_x, source_y)] = 0
shortest_path[(source_x, source_y)] = 0

while (destination_x, destination_y) not in shortest_path:
    next_node = [k for k, x in distances.items() if not any(y < x for y in distances.values())][0]
    get_adjacent_vertices(next_node, corrupted_spaces, shortest_path, distances)
    shortest_path[next_node] = distances[next_node]
    distances.pop(next_node)

end = time.time()
print("Part 1 result: {}".format(shortest_path[(destination_x, destination_y)]))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()