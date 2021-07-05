# test_primes.py

from Primes import Primes

def test():
    P = Primes()
    limits = [10 ** i for i in range(6)]

    for lim in limits:
        P.calcPrimes(lim)
        primes = P.getPrimes()
        print("limit: {0:.1e}, number of primes: {1}".format(lim, len(primes)))
    
test()

