# prob_003.py

# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#

def divisors(number):
    divs = [x for x in range(1, number//2 + 1) if number % x == 0]
    divs.append(number)
    return divs

def isPrime(number):
    # note: 1 is not prime
    divs = divisors(number)
    if len(divs) == 2:
        return True
    else:
        return False

def getPrimes(max_val):
    primes = [x for x in range(1, max_val + 1) if isPrime(x)]
    return primes

def solve_v1(number):
    # loop over divisors, check which are prime
    primeFactors = []
    divs = divisors(number)
    for x in divs:
        if isPrime(x):
            primeFactors.append(x)
    return primeFactors

def solve_v2(number):
    # loop over primes, check which are divisors
    primeFactors = []
    primes = getPrimes(10**4)
    i = 0
    while i < len(primes) and primes[i] <= number // 2:
        if number % primes[i] == 0:
            primeFactors.append(primes[i])
        i += 1
    return primeFactors

#primes = getPrimes(10**4)
#print(primes)
#print("number of primes: {0}".format(len(primes)))

#x = solve_v1(13195)
#print("prime factors: {0}".format(x))
#print("largest prime factor: {0}".format(max(x)))
#
#x = solve_v2(13195)
#print("prime factors: {0}".format(x))
#print("largest prime factor: {0}".format(max(x)))

#x = solve_v1(600851475143)
#print("prime factors: {0}".format(x))
#print("largest prime factor: {0}".format(max(x)))

x = solve_v2(600851475143)
print("prime factors: {0}".format(x))
print("largest prime factor: {0}".format(max(x)))

