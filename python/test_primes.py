# test_primes.py

from Primes import Primes
import time

def test():
    P = Primes()
    limits = [10 ** i for i in range(7)]

    t0 = time.time()
    
    for lim in limits:
        P.calcPrimesBasic(lim)
        primes = P.getPrimes()
        print("limit: {0:.1e}, number of primes: {1}".format(lim, len(primes)))
        #print(primes)

    t1 = time.time()
    
    run_time = t1 - t0
    print("run time: {0:.3f} seconds".format(run_time))
    
    for lim in limits:
        P.calcPrimesAdvanced(lim)
        primes = P.getPrimes()
        print("limit: {0:.1e}, number of primes: {1}".format(lim, len(primes)))
        #print(primes)
    
    t2 = time.time()
    
    run_time = t2 - t1
    print("run time: {0:.3f} seconds".format(run_time))
    
test()

