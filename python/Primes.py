# Primes.py

import numpy as np

class Primes:
    def __init__(self):
        self.primes = []

    # find number of divisors
    def divisors(self, number):
        divs = [x for x in range(1, number//2 + 1) if number % x == 0]
        divs.append(number)
        return divs

    # does number have exactly two divisors
    def twoDivs(self, number):
        divs = self.divisors(number)
        if len(divs) == 2:
            return True
        else:
            return False

    # does number have divisors up to square root of number
    def divsToSqrt(self, number):
        i = 2
        while i <= int(np.sqrt(number)):
            if number % i == 0:
                return True
            i += 1
        # no divisors up to square root of number
        return False
    
    def isPrime(self, number, values=[]):
        # note: 1 is not prime
        # speed up by checking some divisors
        if number == 1:
            return False
        if values:
            if number in values:
                return True
            for v in values:
                if number % v == 0:
                    return False
        
        # check for divisors up to square root
        return not self.divsToSqrt(number)

    def calcPrimes(self, max_val):
        if max_val > 1000:
            # speed up by using first set of primes
            first_max = 1000
            first_primes    = [x for x in range(1, first_max) if self.isPrime(x)]
            second_primes   = [x for x in range(first_max, max_val) if self.isPrime(x, first_primes)]
            primes = first_primes + second_primes
        else:
            primes = [x for x in range(1, max_val) if self.isPrime(x)]
        self.setPrimes(primes)

    def setPrimes(self, primes):
        self.primes = primes

    def getPrimes(self):
        return self.primes

