# python/prob_031.py

# Problem 31

# In the United Kingdom the currency is made up of pound (£) and pence (p). 
# There are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

from Solver import Solver

def solve(total):
    print("Solving for total = {0}".format(total))
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = []
    for coin in coins:
        s = 0
        count = 0
        while s < total:
            s += coin
            count += 1
        if s == total:
            ways.append(count)
    n_ways = len(ways)
    print(ways)
    return n_ways

def main():
    solver = Solver(solve, 200)
    solver.solve()

main()

