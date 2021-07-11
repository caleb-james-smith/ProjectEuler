# prob_005.py

# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#

from Solver import Solver

def solve(max_val):
    search = True
    i = 1
    values = range(1, max_val + 1)
    answer = -1
    while search:
        divisible = True
        for v in values:
            if not i % v == 0:
                divisible = False
                break
        if divisible:
            search = False
            answer = i
        i += 1
    return answer

def main():
    solver = Solver(solve, 20)
    solver.solve()

main()

