import time
import os
import math
from collections import defaultdict

class PseudoRandomizer:

    def __init__(self, initial_secret):
        self.__secret = initial_secret
        self.__prices = [self.__secret % 10]

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
        # store the last digit of the secret as the price expressed in bananas count
        self.__prices.append(self.__secret % 10)

    def get_secret(self):
        return self.__secret

    def set_secret(self, s):
        self.__secret = s

    def get_prices(self):
        return self.__prices

    def get_price_changes(self):
        return [self.__prices[j] - self.__prices[j-1] for j in range(1, len(self.__prices))]

    def __str__(self):
        return str(self.__secret)

start = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 22"), 'r')
numbers = [int(n) for n in file.read().split("\n")]

sum_of_last_secret = 0
bananas_counter = defaultdict(int)
for n in numbers:
    r = PseudoRandomizer(n)
    for i in range(0, 2000):
        r.next_secret()
    sum_of_last_secret += r.get_secret()

    price_changes = r.get_price_changes()
    prices = r.get_prices()[1:]
    seq_seen = set()
    for i in range(0, len(price_changes) - 4, 1):
        seq = ", ".join([str(i) for i in price_changes[i:i + 4]])
        # Check to only consider the first occurrence of a price changes sequence
        if seq not in seq_seen:
            bananas_counter[seq] += prices[i + 3]
            seq_seen.add(seq)

print("Part 1 result: {}".format(sum_of_last_secret))
print()

# Get the sequence of price changes with the maximum banana count overall
max_key = ""
bananas = 0
for k, v in bananas_counter.items():
    if v > bananas:
        max_key, bananas = k, v

end = time.time()
print("Part 2 result: {}".format(bananas_counter[max_key]))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()

