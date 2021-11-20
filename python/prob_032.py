# prob_032.py

# Problem 32
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 × 186 = 7254,
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# 
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# 
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
#

# a x b = c
# total number of digits: 9
# must be 1-9 pandigital

from Solver import Solver
from tools import pandigital

def solve(max_val):
    result = -1
    tot_dig = 9
    for a_num_dig in range(1, 8):
        for b_num_dig in range(a_num_dig, 8):
            c_num_dig = tot_dig - a_num_dig - b_num_dig
            if c_num_dig < 1:
                continue
            print("({0}, {1}, {2})".format(a_num_dig, b_num_dig, c_num_dig))
    return result

def main():
    solver = Solver(solve, 10**9)
    solver.solve()

main()

