import time
import os

def blink(arr):
    new_arr = []
    for i in range(0, len(arr)):
        digit_len = len("" + str(arr[i]))
        if arr[i] == 0:
            new_arr.append(1)
        elif digit_len % 2 == 0:
            _tmp = "" + str(arr[i])
            new_arr.append(int(_tmp[:digit_len//2]))
            new_arr.append(int(_tmp[digit_len//2:]))
        else:
            new_arr.append(arr[i]*2024)
    return new_arr


start_p1 = time.time()
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 11"), 'r') as file:
    arrangement = [int(i) for i in file.read().replace("\n", "").split(" ")]

for k in range(0, 25):
    arrangement = blink(arrangement)

end_p1 = time.time()
print("Part 1 result: {}".format(len(arrangement)))
print("The time of execution of above program is :", (end_p1 - start_p1) * 10**3, "ms")
print()
