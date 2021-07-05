# Primes.py

class Primes:
    def __init__(self):
        self.primes = []

    def divisors(self, number):
        divs = [x for x in range(1, number//2 + 1) if number % x == 0]
        divs.append(number)
        return divs

    def twoDivs(self, number):
        # does number have two divisors
        divs = self.divisors(number)
        if len(divs) == 2:
            return True
        else:
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
        # check number of divisors
        return self.twoDivs(number)

    def calcPrimes(self, max_val):
        first_max = 1000
        first_primes    = [x for x in range(1, first_max) if self.isPrime(x)]
        second_primes   = [x for x in range(first_max, max_val + 1) if self.isPrime(x, first_primes)]
        primes = first_primes + second_primes
        self.setPrimes(primes)

    def setPrimes(self, primes):
        self.primes = primes

    def getPrimes(self):
        return self.primes

