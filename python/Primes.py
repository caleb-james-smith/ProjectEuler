# Primes.py

class Primes:
    def __init__(self):
        self.primes = []

    def divisors(self, number):
        divs = [x for x in range(1, number//2 + 1) if number % x == 0]
        divs.append(number)
        return divs
    
    def isPrime(self, number):
        # note: 1 is not prime
        divs = self.divisors(number)
        if len(divs) == 2:
            return True
        else:
            return False

    def calcPrimes(self, max_val):
        primes = [x for x in range(1, max_val + 1) if self.isPrime(x)]
        self.setPrimes(primes)

    def setPrimes(self, primes):
        self.primes = primes

    def getPrimes(self):
        return self.primes

