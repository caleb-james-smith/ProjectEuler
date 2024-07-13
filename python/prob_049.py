# python/prob_049.py

# Problem 49

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i)   each of the three terms are prime, and,
# (ii)  each of the 4-digit numbers are permutations of one another.
# 
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.
# 
# What 12-digit number do you form by concatenating the three terms in this sequence?

from Primes import Primes
from Solver import Solver
 
# check if number has specified number of digits
def hasNumDigits(number, ndigits):
    s = str(number)
    if len(s) == ndigits:
        return True
    else:
        return False

# count number of occurances of digit
def countDigOcc(digit, number):
    count = 0
    s = str(digit)
    if len(s) != 1:
        print("ERROR: s = {0} does not have a length of 1.".format(s))
    for x in str(number):
        if x == s:
            count += 1
    return count

# check that two numbers have the same digits
# required that numbers are same length
def hasSameDigits(n1, n2):
    s1 = str(n1)
    s2 = str(n2)
    len_1 = len(s1)
    len_2 = len(s2)
    
    # require same length
    if len_1 != len_2:
        False
    
    # need to check both ways...
    # does not account for difference in number of occurances of digit
    #for x in s1:
    #    if x not in s2:
    #        return False
    #for x in s2:
    #    if x not in s1:
    #        return False

    for x in s1:
        c1 = countDigOcc(x, s1) 
        c2 = countDigOcc(x, s2) 
        if c1 != c2:
            return False

    return True

# check if list is arithmetic sequence
def isArithSeq(vals):
    n_vals = len(vals)
    if n_vals < 2:
        return False
    else:
        first_diff = vals[1] - vals[0]
        for i in range(1, n_vals - 1):
            diff = vals[i + 1] - vals[i]
            if diff != first_diff:
                return False
        return True

def solve(ndigits):
    answer = ""
    print("Solving for ndigits = {0}".format(ndigits))
    max_val = 10 ** ndigits
    P = Primes()
    P.calcPrimesAdvanced(max_val)
    primes = P.getPrimes()
    n_primes = len(primes)

    # get primes with number of digits
    selected_primes = [p for p in primes if hasNumDigits(p, ndigits)] 
    n_selected_primes = len(selected_primes)
    print("Number of primes with {0} digits: {1}".format(ndigits, n_selected_primes))
    
    for i in range(n_selected_primes):
        p1 = selected_primes[i]
        matches = [p1]
        for j in range(i + 1, n_selected_primes):
            p2 = selected_primes[j]
            if hasSameDigits(p1, p2):
                matches.append(p2)
        
        n_matches = len(matches)
        
        #print("p1 = {0}, n_matches = {1}".format(p1, n_matches))
        #print(matches)

        # TODO: does not find the example answer yet
        #       need to check cases with matches > 3

        if n_matches == 3:
            if isArithSeq(matches):
                print("p1 = {0}, n_matches = {1}".format(p1, n_matches))
                print(matches)
                strings = [str(x) for x in matches]
                answer = "".join(strings)
    return answer

def main():
    solver = Solver(solve, 4)
    solver.solve()

main()

