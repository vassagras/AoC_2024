import time
import os

start = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 25"), 'r')
content = file.read().split("\n")

lock_heights = []
key_heights = []
for i in range(0, len(content), 8):
    # it is a lock
    if content[i] == "#####":
        heights = []
        for k in range(0, 5):
            # ignore the first row in the height calculation (start from i+1)
            col_k = [content[i + 1 + j][k] for j in range(0, 6) if content[i + 1 + j][k] == "#"]
            heights.append(len(col_k))
        lock_heights.append(heights)
    # it is a key
    elif content[i] == ".....":
        heights = []
        for k in range(0, 5):
            col_k = [content[i + j][k] for j in range(0, 6) if content[i + j][k] == "#"]
            heights.append(len(col_k))
        key_heights.append(heights)

number_of_overlaps = 0
for lock in lock_heights:
    for key in key_heights:
        key_lock = list(map(lambda x, y: x + y, lock, key))
        if all(e <= 5 for e in key_lock):
            number_of_overlaps += 1

end = time.time()
print("Part 1 result: {}".format(number_of_overlaps))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()