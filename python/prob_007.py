# prob_007.py

# Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
#

from Primes import Primes
from Solver import Solver

def solve(parameters):
    max_val = parameters[0]
    index   = parameters[1]
    P = Primes()
    P.calcPrimesAdvanced(max_val)
    primes = P.getPrimes()
    result = primes[index - 1]
    return result

def main():
    solver = Solver(solve, [10**6, 10001])
    solver.solve()

main()
