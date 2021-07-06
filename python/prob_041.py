# prob_041.py

# Problem 41
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?
#

from Primes import Primes
import time

def pandigital(number):
    s = str(number)
    for i in range(1, len(s) + 1):
        if str(i) not in s:
            return False
    return True

def solve(max_val):
    P = Primes()
    P.calcPrimesAdvanced(max_val)
    primes = P.getPrimes()
    largest_val = -1
    for p in primes:
        if pandigital(p):
            if p > largest_val:
                largest_val = p
    return largest_val

def main():
    start_time = time.time()
    x = solve(10**9)
    end_time = time.time()
    
    run_time = end_time - start_time 
    
    print("answer: {0}".format(x))
    print("run time: {0:.3f} seconds".format(run_time))

main()

