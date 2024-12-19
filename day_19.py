import time
import os

def check_for_matching_towels(cur_design, patterns, pattern_cache):
    """
        :param cur_design: current design  to be assessed
        :param patterns: available towel patterns
        :param pattern_cache: cache with the already assessed designs
        :return: the number of towel / pattern arrangements matching the design or 0 if there is no match
        """
    # all letters of the design have been matched with one or multiple towels
    if len(cur_design) == 0:
        return 1

    # if the current design (full or sub-design) has already been assessed, there is not need to do it again
    if cur_design in pattern_cache:
        return pattern_cache[cur_design]

    match_count = 0
    for towel in patterns:
        if cur_design.startswith(towel):
            if check_for_matching_towels(cur_design[len(towel):], patterns, pattern_cache) > 0:
                match_count += check_for_matching_towels(cur_design[len(towel):], patterns, pattern_cache)
    pattern_cache[cur_design] = match_count
    return match_count

start = time.time()
file_designs = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 19 designs"), 'r')
file_patterns = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 19 patterns"), 'r')

towel_patterns = file_patterns.read().replace("\n", "").split(", ")
designs = []
for design in file_designs:
    designs.append(design.replace("\n", ""))

matched_designs = []
cache = {}
for design in designs:
    if check_for_matching_towels(design, towel_patterns, cache) > 0:
        matched_designs.append(design)

end = time.time()
print("Part 1 result: {}".format(len(matched_designs)))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()

start = time.time()

matched_designs = []
cache = {}
number_of_arrangements = 0
for design in designs:
    number_of_arrangements += check_for_matching_towels(design, towel_patterns, cache)

end = time.time()
print("Part 2 result: {}".format(number_of_arrangements))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()