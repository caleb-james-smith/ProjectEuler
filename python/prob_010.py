# prob_010.py

# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#

from Primes import Primes
from Solver import Solver

def solve(max_val):
    P = Primes()
    P.calcPrimesAdvanced(max_val)
    primes = P.getPrimes()
    result = sum(primes)
    return result

def main():
    solver = Solver(solve, 2 * 10**6)
    solver.solve()

main()

