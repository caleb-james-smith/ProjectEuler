# prob_003.py

# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#

from Primes import Primes 

def solve(number, primes):
    # loop over primes, check which are divisors
    # search up to number in case number is prime
    primeFactors = []
    i = 0
    while i < len(primes) and primes[i] <= number:
        if number % primes[i] == 0:
            primeFactors.append(primes[i])
        i += 1
    return primeFactors

max_val = 10**7
P = Primes()
#P.calcPrimesBasic(max_val)
P.calcPrimesAdvanced(max_val)
primes = P.getPrimes()
print("number of primes less than {0}: {1}".format(max_val, len(primes)))

#x = solve(13195, primes)
#print("prime factors: {0}".format(x))
#print("largest prime factor: {0}".format(max(x)))

x = solve(600851475143, primes)
print("prime factors: {0}".format(x))
print("largest prime factor: {0}".format(max(x)))

#numbers = [
#    101,
#    10101,
#    1010101,
#    101010101,
#    10101010101,
#]
#for n in numbers:
#    print("{0}: {1}".format(n, solve(n, primes)))

