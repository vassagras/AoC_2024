import functools
from collections import Counter
import time
import os

def is_report_valid(_report) -> bool:
    diff = []
    diff_abs = []
    for i in range(0, len(_report) - 1):
        diff.append(_report[i] - _report[i + 1])
        diff_abs.append(abs(_report[i] - _report[i + 1]))

    if all(val > 0 for val in diff):
        if all(val <= 3 for val in diff_abs):
            return True
    if all(val < 0 for val in diff):
        if all(val <= 3 for val in diff_abs):
            return True
    return False

start = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 02"), 'r')

counter = 0
for l in file:
    report = list(map(int, l.split()))
    if is_report_valid(report):
        counter += 1

end = time.time()
print("Part 1 result: {}".format(counter))
print("The time of execution of above program is :", (end-start) * 10**3, "ms")
print()

def is_report_valid_part_2(_report) -> bool:
    for i in range(len(_report)):
        # Remove one level and check if the new report is now safe
        modified_report = _report[:i] + _report[i + 1:]
        if is_report_valid(modified_report):
            return True
    return False

start = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 02"), 'r')
counter_2 = 0
for l in file:
    report = list(map(int, l.split()))
    if is_report_valid_part_2(report):
        counter_2 += 1

end = time.time()
print("Part 2 result: {}".format(counter_2))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()
