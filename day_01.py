"""
Usage of Counter class to optimize the count of a hashable object.

Counter is a subclass of dict that’s specially designed for counting hashable objects in Python.
It’s a dictionary that stores objects as keys and counts as values.
To count with Counter, you typically provide a sequence or iterable of hashable objects
as an argument to the class’s constructor

https://realpython.com/python-counter/
"""

import functools
from collections import Counter
import time
import os

file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 01"), 'r')

left = []
right = []

for l in file:
    left.append(int(l.split()[0]))
    right.append(int(l.split()[1]))

left_sorted = sorted(left)
right_sorted = sorted(right)

diff = 0
for i in range(len(right_sorted)):
    diff += abs(left_sorted[i] - right_sorted[i])

print("Part 1 result: {}".format(diff))
print()

# Part 2
def similarity_score(list_1, list_2) -> int:
    return functools.reduce(lambda x,y: x+y, [e*list_2.count(e) for e in list_1])

def similarity_score_v2(list_1, list_2) -> int:
    counter = Counter(list_2)
    return sum([e*counter[e] for e in list_1])

start_p2 = time.time()
print("Part 2 result: {}".format(similarity_score(left, right)))
end_p2 = time.time()
print("The time of execution of above program is :", (end_p2-start_p2) * 10**3, "ms")
print()

start_p2 = time.time()
print("Part 2 with Counter result: {}".format(similarity_score_v2(left, right)))
end_p2 = time.time()
print("The time of execution of above program is {} ms".format((end_p2-start_p2) * 10**3))