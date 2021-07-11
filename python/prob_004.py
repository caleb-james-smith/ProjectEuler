# prob_004.py

# Problem 4
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#

from Solver import Solver

# check if number reads the same both ways
def palindrome(number):
    s = str(number)
    return s == s[::-1]

def solve(num_digits):
    current_max = -1
    limit = 10 ** num_digits
    for i in range(1, limit):
        for j in range(i, limit):
            product = i * j
            if palindrome(product):
                if product > current_max:
                    current_max = product
    return current_max

def main():
    solver = Solver(solve, 3)
    solver.solve()

main()

