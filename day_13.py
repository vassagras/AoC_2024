import time
import re
import os
from sympy import symbols, Eq, solve, Integer
start = time.time()
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 13"), 'r') as f:
    lines = f.readlines()

part_1_sum = 0
part_2_sum = 0
regex_buttons = r"Button (A|B): X\+(\d*), Y\+(\d*)"
regex_results = r"Prize: X=(\d*), Y=(\d*)"
# Read the lines by 3 and create a system of two equations and two variables
for i in range(0, len(lines), 4):
    elements = re.findall(regex_buttons, lines[i])
    _a1, _a2 = [int(i) for i in elements[0][1:]]
    elements = re.findall(regex_buttons, lines[i+1])
    _b1, _b2 = [int(i) for i in elements[0][1:]]
    elements = re.findall(regex_results, lines[i+2])
    _c1, _c2 = [int(i) for i in elements[0]]
    # For part 2
    __c1, __c2 = [int(i) + 10000000000000 for i in elements[0]]
    x, y = symbols("x,y")
    eq1 = Eq((_a1*x + _b1*y), _c1)
    eq2 = Eq((_a2 * x + _b2 * y), _c2)
    sol = solve((eq1, eq2), (x, y))
    # Consider only equations with integer solutions
    if isinstance(sol[x], Integer) and isinstance(sol[y], Integer):
        part_1_sum += 3*sol[x] + sol[y]
    eq1 = Eq((_a1 * x + _b1 * y), __c1)
    eq2 = Eq((_a2 * x + _b2 * y), __c2)
    sol = solve((eq1, eq2), (x, y))
    # Consider only equations with integer solutions
    if isinstance(sol[x], Integer) and isinstance(sol[y], Integer):
        part_2_sum += 3 * sol[x] + sol[y]

end = time.time()
print("Part 1 result: {}".format(part_1_sum))
print()
print("Part 2 result: {}".format(part_2_sum))
print("The time of execution of above program is :", (end - start) * 10**3, "ms")
print()
