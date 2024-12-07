import time
import itertools

def compute_equation(elements, operators):
    """

    :param elements: numbers for calculating the test value
    :param operators: operator combination
    :return: result of the equation
    """
    _result = elements[0]
    for i in range(1, len(elements)):
        if operators[i-1] == "+":
            _result += elements[i]
        else:
            _result *= elements[i]
    return _result

def compute_equation_v2(elements, operators):
    """

    :param elements: numbers for calculating the test value
    :param operators: operator combination
    :return: result of the equation
    """
    _result = elements[0]
    for i in range(1, len(elements)):
        if operators[i-1] == "+":
            _result += elements[i]
        elif operators[i-1] == "*":
            _result *= elements[i]
        else:
            _result = int(str(_result) + str(elements[i]))
    return _result

start = time.time()
file = open(r'C:\Users\vassi\dev\PythonVarious\Advent of Code 2024\inputs\Day 7', 'r')
p1_sum, p2_sum = 0, 0
p1_ops, p2_ops = ["+", "*"], ["+", "*", "||"]
for l in file:
    test_value = int(l.split(":")[0])
    numbers = [int(n) for n in l.split(":")[1].strip().split()]
    permutations = list(itertools.product(p1_ops, repeat=len(numbers) - 1))
    control_flag = False
    for perm in permutations:
        r = compute_equation(numbers, perm)
        if r == test_value:
            p1_sum += test_value
            control_flag = True
            break

    if not control_flag:
        permutations_v2 = list(itertools.product(p2_ops, repeat=len(numbers) - 1))
        for perm in permutations_v2:
            r = compute_equation_v2(numbers, perm)
            if r == test_value:
                p2_sum += test_value
                break
final_result = p1_sum + p2_sum

end = time.time()
print("Part 1 result: {}".format(p1_sum))
print("Part 2 result: {}".format(final_result))
print("The time of execution of above program is :", (end - start) * 10**3, "ms")
print()

