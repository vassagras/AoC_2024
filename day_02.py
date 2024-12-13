import functools
from collections import Counter
import time
import os

def is_report_valid(report) -> bool:
    diff = []
    diff_abs = []
    for i in range(0, len(report) - 1):
        diff.append(report[i] - report[i+1])
        diff_abs.append(abs(report[i] - report[i+1]))

    if all(val > 0 for val in diff):
        if all(val <= 3 for val in diff_abs):
            return True
    if all(val < 0 for val in diff):
        if all(val <= 3 for val in diff_abs):
            return True
    return False

file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 02"), 'r')


start_p1 = time.time()
counter = 0
for l in file:
    report = list(map(int, l.split()))
    if is_report_valid(report):
        counter += 1

end_p1 = time.time()
print("Part 1 result: {}".format(counter))
print("The time of execution of above program is :", (end_p1-start_p1) * 10**3, "ms")
print()
'''

def is_report_valid_part_2(arr) -> bool:
    diff = []
    diff_abs = []
    for i in range(0, len(arr) - 1):
        diff.append(arr[i] - arr[i + 1])
        diff_abs.append(abs(arr[i] - arr[i + 1]))

    print(report)
    print(diff)
    print(diff_abs)
    if len(list(filter(lambda x: x <= 0, diff))) > 1:
        return False
    if len(list(filter(lambda x: x > 3, diff_abs))) > 1:
        return False

    return True

start_p2 = time.time()
counter2 = 0
for l in file:
    report = list(map(int, l.split()))
    if is_report_valid_part_2(report):
        counter2 += 1
        print("Safe")
        print()

end_p2 = time.time()
print("Part 2 result: {}".format(counter2))
print("The time of execution of above program is :", (end_p2 - start_p2) * 10**3, "ms")
print()'''
