import time
import os
import math

class PseudoRandomizer:

    def __init__(self, initial_secret):
        self.__secret = initial_secret

    def mix(self, result):
        self.__secret = result ^ self.__secret

    def prune(self):
        self.__secret = self.__secret % 16777216

    def next_secret(self):
        self.mix(self.__secret * 64)
        self.prune()
        self.mix(math.floor(self.__secret / 32))
        self.prune()
        self.mix(self.__secret * 2048)
        self.prune()

    def get_secret(self):
        return self.__secret

    def set_secret(self, s):
        self.__secret = s

    def __str__(self):
        return str(self.__secret)

start = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 22"), 'r')
numbers = [int(n) for n in file.read().split("\n")]

total = 0
for n in numbers:
    r = PseudoRandomizer(n)
    for i in range(0, 2000):
        r.next_secret()
    total += r.get_secret()

end = time.time()
print("Part 1 result: {}".format(total))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()