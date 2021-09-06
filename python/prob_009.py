# prob_009.py

# Problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#
# Find the product abc.
#

from Solver import Solver

def isTriplet(a, b, c):
    return a**2 + b**2 == c**2

# brute force
def run_v1(target_val):
    result = -1
    max_val_a = target_val // 3
    max_val_b = target_val // 2
    max_val_c = target_val // 1
    for a in range(1, max_val_a):
        for b in range(a + 1, max_val_b):
            for c in range(b + 1, max_val_c):
                if isTriplet(a, b, c):
                    s = a + b + c
                    p = a * b * c
                    print("(a, b, c): ({0}, {1}, {2}), sum = {3}, product = {4}".format(a, b, c, s, p))
                    if s == target_val:
                        result = p
                        return result
    return result

# optimize
def run_v2(target_val):
    result = -1
    max_val_a = target_val // 3
    max_val_b = target_val // 2
    for a in range(1, max_val_a):
        for b in range(a + 1, max_val_b):
            # require "a + b + c = target value" to eliminate loop over "c"
            c = target_val - a - b
            if isTriplet(a, b, c):
                s = a + b + c
                p = a * b * c
                print("(a, b, c): ({0}, {1}, {2}), sum = {3}, product = {4}".format(a, b, c, s, p))
                result = p
                return result
    return result

def solve(target_val):
    #result = run_v1(target_val)
    result = run_v2(target_val)
    return result

def main():
    solver = Solver(solve, 10**3)
    solver.solve()

main()

