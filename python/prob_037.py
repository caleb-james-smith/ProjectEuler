# prob_037.py

# Problem 37
#
# The number 3797 has an interesting property.
# Being prime itself, it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
#

from Primes import Primes
from Solver import Solver

# check for left to right truncatable
def isLRT(number, primes):
    num_s   = str(number)
    num_len = len(num_s) 
    if num_len < 2:
        return False
    for i in range(num_len):
        s = num_s[i:]
        n = int(s)
        if n not in primes:
            return False
    return True

# check for right to left truncatable
def isRLT(number, primes):
    num_s   = str(number)
    num_len = len(num_s) 
    if num_len < 2:
        return False
    if number not in primes: 
        return False
    for i in range(1, num_len):
        s = num_s[:-i]
        n = int(s)
        if n not in primes:
            return False
    return True

def solve(max_val):
    result = 0
    count  = 0
    P = Primes()
    P.calcPrimesAdvanced(max_val)
    primes = P.getPrimes()
    for prime in primes:
        if isLRT(prime, primes) and isRLT(prime, primes):
            result += prime
            count += 1
            print(prime)
    print("count: {0}".format(count))
    return result

def main():
    solver = Solver(solve, 10**6)
    solver.solve()

main()

