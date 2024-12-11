import time
import os
from collections import Counter

def blink(stones):
    new_arr = []
    for i in range(0, len(stones)):
        digit_len = len(str(stones[i]))
        if stones[i] == 0:
            new_arr.append(1)
        elif digit_len % 2 == 0:
            _tmp = "" + str(stones[i])
            new_arr.append(int(_tmp[:digit_len//2]))
            new_arr.append(int(_tmp[digit_len//2:]))
        else:
            new_arr.append(stones[i] * 2024)
    return new_arr

start = time.time()
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 11"), 'r') as file:
    arrangement = [int(i) for i in file.read().replace("\n", "").split(" ")]

for k in range(0, 25):
    arrangement = blink(arrangement)

end = time.time()
print("Part 1 result: {}".format(len(arrangement)))
print("The time of execution of above program is :", (end - start) * 10**3, "ms")
print()

start = time.time()
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 11"), 'r') as file:
    arrangement = [int(i) for i in file.read().replace("\n", "").split(" ")]

# Avoid repeating the same calculation by using a Counter to group the same numbers / elements
master_counter = Counter(arrangement)
for k in range(0, 75):
    new_counter = Counter()
    for elem, cnt in master_counter.items():
        if elem == 0:
            new_counter[1] += cnt
        elif len(str(elem)) % 2 == 0:
            l = len(str(elem))
            new_counter[int(str(elem)[:l // 2])] += cnt
            new_counter[int(str(elem)[l // 2:])] += cnt
        else:
            new_counter[elem * 2024] += cnt
    master_counter = new_counter

end = time.time()
print("Part 2 result: {}".format(sum(master_counter.values())))
print("The time of execution of above program is :", (end - start) * 10**3, "ms")
print()
