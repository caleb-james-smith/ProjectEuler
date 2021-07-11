# prob_034.py

# Problem 34
#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.
#

from Solver import Solver

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sumOfFactorials(number):
    s = str(number)
    values = [factorial(int(x)) for x in s]
    return sum(values)

def solve(max_val):
    values = []
    for i in range(10, max_val):
        if sumOfFactorials(i) == i:
            values.append(i)
    print(values)
    return(sum(values))

def main():
    solver = Solver(solve, 10**7)
    solver.solve()

main()

