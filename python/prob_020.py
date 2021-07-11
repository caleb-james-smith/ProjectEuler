# prob_020.py

# Problem 20
#
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
#

from Solver import Solver

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def solve(max_val):
    x = factorial(max_val)
    s = str(x)
    values = [int(y) for y in s]
    return sum(values)

def main():
    solver = Solver(solve, 100)
    solver.solve()

main()

