# Primes.py

import numpy as np

class Primes:
    def __init__(self):
        self.primes = []

    # find divisors of a number
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
        if number == 1:
            return False
        # speed up by checking some divisors from list of primes
        if values:
            if number in values:
                return True
            for v in values:
                if number % v == 0:
                    return False
        
        # check for divisors up to square root
        return not self.divsToSqrt(number)

    # Basic algorithm: find primes in two sets, and use first set to speed up second set
    def calcPrimesBasic(self, max_val):
        if max_val > 1000:
            # speed up by using first set of primes
            first_max = 1000
            first_primes    = [x for x in range(1, first_max) if self.isPrime(x)]
            second_primes   = [x for x in range(first_max, max_val) if self.isPrime(x, first_primes)]
            primes = first_primes + second_primes
        else:
            primes = [x for x in range(1, max_val) if self.isPrime(x)]
        self.setPrimes(primes)

    # Sieve of Eratosthenes
    def calcPrimesAdvanced(self, max_val):
        if max_val < 1:
            print("ERROR: max_val needs to be a positive integer")
            return
        elif max_val == 1:
            self.setPrimes([])
            return
        # start with all numbers assigned True for prime
        # assign False to numbers that are divisible 
        # at the end, numbers still assigned True are prime
        is_prime_list = max_val * [True]
        is_prime_list[0] = False 
        is_prime_list[1] = False 
        # check up to square root of number
        for i in range(2, int(np.sqrt(max_val)) + 1):
            if is_prime_list[i]:
                # start from i^2 to save time
                for j in range(i**2, max_val, i):
                    is_prime_list[j] = False
        primes = [i for i in range(len(is_prime_list)) if is_prime_list[i]] 
        self.setPrimes(primes)

    def setPrimes(self, primes):
        self.primes = primes

    def getPrimes(self):
        return self.primes

