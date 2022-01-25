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

def run(digits):
    result = []
    a_num_dig = digits[0]
    b_num_dig = digits[1]
    c_num_dig = digits[2]
    for a in range(10**(a_num_dig-1), 10**a_num_dig):
        for b in range(10**(b_num_dig-1), 10**b_num_dig):
            c = a * b
            all_dig = str(a) + str(b) + str(c)
            if not pandigital(all_dig):
                continue
            result.append(c)
            print("{0} * {1} = {2}".format(a, b, c))
    return result

# TODO: avoid double counting products that come from different multiples
def solve(max_val):
    products = []
    result = 0
    tot_dig = 9
    for a_num_dig in range(1, 8):
        for b_num_dig in range(a_num_dig, 8):
            c_num_dig = tot_dig - a_num_dig - b_num_dig
            if c_num_dig < 1:
                continue
            if a_num_dig + b_num_dig < c_num_dig:
                continue
            if a_num_dig + b_num_dig > c_num_dig + 1:
                continue
            print("({0}, {1}, {2})".format(a_num_dig, b_num_dig, c_num_dig))
            digits = [a_num_dig, b_num_dig, c_num_dig]
            values = run(digits)
            for v in values:
                if v not in products:
                    products.append(v)
    result = sum(products)
    return result

def main():
    solver = Solver(solve, 10**9)
    solver.solve()

main()

