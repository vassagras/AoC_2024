import collections
import time
import os

start_p1 = time.time()

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 09"), 'r') as file:
    disk_map = file.read()

blocks = []
free_space_indexes = []
id_nbr = 0
index = 0
space_flag = False

for c in disk_map:
    if space_flag:
        if c != "0":
            for i in range(0, int(c)):
                blocks.append(".")
                free_space_indexes.append(index)
                index += 1
        space_flag = False
    else:
        if c!= "0":
            for i in range(0, int(c)):
                blocks.append(str(id_nbr))
                index += 1
        space_flag = True
        id_nbr += 1

print("".join(blocks))

main_index = len(blocks) - 1
for i in range(0, len(free_space_indexes)):
    free_space_index = free_space_indexes[i]
    while blocks[main_index] == ".":
        main_index -= 1
    if main_index < free_space_index:
        break
    blocks[free_space_index] = blocks[main_index]
    blocks[main_index] = "."
    #print("".join(blocks))

print("".join(blocks))
checksum = sum([i*int(val) for i, val in enumerate(blocks[:main_index+1])])

end_p1 = time.time()
print("Part 1 result: {}".format(checksum))
print("The time of execution of above program is :", (end_p1 - start_p1) * 10**3, "ms")
print()


