import time
import os
from networkx import DiGraph
from itertools import combinations

start = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 23"), 'r')

# Create a directed graph
network = DiGraph()
nodes = set()
for line in file:
    node_1, node_2 = line.replace("\n", "").split("-")
    network.add_edge(node_1, node_2)
    network.add_edge(node_2, node_1)
    nodes.update([node_1, node_2])
print(network)
print()

# identify all the valid triplets i.e., having at least a node / computer starting with t
list_of_nodes = list(nodes)
triplets = [triplet for triplet in combinations(list_of_nodes, 3)
            if any([n.startswith("t") for n in triplet])]

inter_connected_sets = 0
for combination in triplets:
    if len(combination) == 3:
        if (network.has_edge(combination[0], combination[1]) and network.has_edge(combination[1], combination[2]) and
                network.has_edge(combination[2], combination[0])):
            inter_connected_sets += 1

end = time.time()
print("Part 1 result: {}".format(inter_connected_sets))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()
