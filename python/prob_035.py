# prob_035.py

# Problem 35
#
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?
#

from Primes import Primes
from Solver import Solver

def circular(number, primes):
    s = str(number)
    n_digits = len(s)
    for i in range(n_digits - 1):
        # rotate digits
        s = s[1:] + s[0]
        n = int(s)
        is_prime = n in primes
        if not is_prime:
            return False
    return True

def solve(max_val):
    P = Primes()
    P.calcPrimesAdvanced(max_val)
    primes = P.getPrimes()
    circular_primes = [x for x in primes if circular(x, primes)]
    print(circular_primes)
    return len(circular_primes)

def main():
    solver = Solver(solve, 10**6)
    solver.solve()

main()

