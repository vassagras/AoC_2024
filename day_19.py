import time
import os

def identify_matching_towels(cur_design, patterns, pattern_cache):
    """
    
    :param cur_design: current design  to be assessed
    :param patterns: available towel patterns
    :param pattern_cache: cache with the already assessed designs
    :return: True if the current design can be reconstructed from the existing patterns
    """
    # all letters of the design have been matched with one or multiple towels
    if len(cur_design) == 0:
        return True

    # if the current design (full or sub-design) has already been assessed, there is not need to do it again
    if cur_design in pattern_cache:
        return pattern_cache[cur_design]

    for towel in patterns:
        if cur_design.startswith(towel):
            if identify_matching_towels(cur_design[len(towel):], patterns, pattern_cache):
                pattern_cache[cur_design[len(towel):]] = True
                return True
    pattern_cache[cur_design] = False
    return False

start = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 19"), 'r')
file_t = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 19 towels"), 'r')

towel_patterns = file_t.read().replace("\n", "").split(", ")
designs = []
for design in file:
    designs.append(design.replace("\n", ""))

matched_designs = []
cache = {}
for design in designs:
    if identify_matching_towels(design, towel_patterns, cache):
        matched_designs.append(design)

end = time.time()
print("Part 1 result: {}".format(len(matched_designs)))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()