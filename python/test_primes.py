# test_primes.py

from Primes import Primes

def test():
    P = Primes()
    P.calcPrimes(10**5)
    primes = P.getPrimes()
    print("number of primes: {0}".format(len(primes)))

test()

