# prob_047.py

# Problem 47
#
# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2^2 × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19
#
# Find the first four consecutive integers to have four distinct prime factors each.
# What is the first of these numbers?
#

from Primes import Primes 

def getPrimeFactors(number, primes):
    # loop over primes, check which are divisors
    # search up to number in case number is prime
    primeFactors = []
    i = 0
    while i < len(primes) and primes[i] <= number:
        if number % primes[i] == 0:
            primeFactors.append(primes[i])
        i += 1
    return primeFactors

def numPrimeFactors(number, primes):
    primeFactors = getPrimeFactors(number, primes)
    return len(primeFactors)

def solve(n_consecutive, n_distinct, primes):
    #for i in range(1, 21):
    #    print("{0}: {1}".format(i, numPrimeFactors(i, primes)))
    search = True
    matches = []
    i = 0
    while search:
        n_factors = numPrimeFactors(i, primes)
        if n_factors == n_distinct:
            matches.append(i)
        else:
            matches = []
        if len(matches) == n_consecutive:
            search = False
        #print("{0}: {1}".format(i, n_factors))
        i += 1
    return matches

P = Primes()
P.calcPrimesAdvanced(10**4)
primes = P.getPrimes()

for i in range(1, 5):
    matches = solve(n_consecutive=i, n_distinct=i, primes=primes)
    print("First {0} consecutive numbers with {0} distinct prime factors: {1}".format(i, matches))

