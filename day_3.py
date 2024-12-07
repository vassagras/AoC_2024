import time
import re

def multiply(arg) -> int:
    return int(arg[4:len(arg)-1].split(",")[0])*int(arg[4:len(arg)-1].split(",")[1])

example = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

start_p1 = time.time()
with open(r'C:\Users\vassi\dev\PythonVarious\Advent of Code 2024\inputs\Day 3', 'r') as file:
    content = file.read()

elements = re.findall(r"(mul\(\d{1,3},\d{1,3}\))", content)

result = 0
for e in elements:
    result += multiply(e)
end_p1 = time.time()

print("Part 1 result: {}".format(result))
print("The time of execution of above program is :", (end_p1 - start_p1) * 10**3, "ms")
print()

start_p2 = time.time()
elements = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))", content)

skip=False
result = 0
for e in elements:
    if e == "don't()":
        skip=True
    elif e == "do()":
        skip=False
    elif not skip:
        result += multiply(e)
end_p2 = time.time()

print("Part 2 result: {}".format(result))
print("The time of execution of above program is :", (end_p2 - start_p2) * 10**3, "ms")
print()
