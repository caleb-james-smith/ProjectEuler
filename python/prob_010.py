# prob_010.py

# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#

from Primes import Primes
import time

def solve(max_val):
    P = Primes()
    P.calcPrimes(max_val)
    primes = P.getPrimes()
    result = sum(primes)
    return result

def main():
    start_time = time.time()
    x = solve(2 * 10**6)
    end_time = time.time()
    
    run_time = end_time - start_time 
    
    print("answer: {0}".format(x))
    print("run time: {0:.3f} seconds".format(run_time))

main()

