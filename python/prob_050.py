# prob_050.py

# Problem 50
#
# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
#

from Primes import Primes
import time

# search for sum of consecutive values that is also in values
def search(length, values):
    for i in range(len(values) - length + 1):
        # sum of consecutive values
        s = sum(values[i:i+length])
        # check if sum is in values
        if s in values:
            return s
    # none found
    return -1

def solve(max_val):
    P = Primes()
    P.calcPrimesAdvanced(max_val)
    primes = P.getPrimes()
    n_primes = len(primes)
    print(n_primes)
    max_length = -1
    max_prime  = -1
    # save time by limiting length
    for length in range(2, 800):
        result = search(length, primes)
        if result > 0:
            if length > max_length:
                max_length = length
                max_prime  = result
    print("max length: {0}, prime: {1}".format(max_length, max_prime))
    return max_prime

def main():
    start_time = time.time()
    x = solve(10**6)
    end_time = time.time()
    
    run_time = end_time - start_time 
    
    print("answer: {0}".format(x))
    print("run time: {0:.3f} seconds".format(run_time))

main()

