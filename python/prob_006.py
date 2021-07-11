# prob_006.py

# Problem 6
#
# The sum of the squares of the first ten natural numbers is 385.
#
# The square of the sum of the first ten natural numbers is 3025.
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#

from Solver import Solver

def solve(max_val):
    values = range(1, max_val + 1)
    # sum of squares
    squares = [x**2 for x in values]
    a = sum(squares)
    # square of sum
    b = sum(values) ** 2
    # difference
    diff = b - a
    return diff

def main():
    solver = Solver(solve, 100)
    solver.solve()

main()
