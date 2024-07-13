# prob_044.py

# Problem 44

# Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:
# 
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
# 
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.
# 
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal
# and D = |Pk − Pj| is minimised; what is the value of D?

from Solver import Solver

# Calculate pentagonal number P(n)
def P(n):
    result = n * (3 * n - 1) / 2 
    result = int(result)
    return result 

def solve(num):
    print("Go go go!")
    result = 1e9
    max_n = int(3e3)
    print("max_n: {0}".format(max_n))
    
    # get pentagonal numbers
    pentagonal_nums = [P(n) for n in range(1, max_n + 1)]
    
    # print pentagonal numbers
    #for i, p in enumerate(pentagonal_nums): 
    #    n = i + 1
    #    print("{0}: {1}".format(n, p))

    # search for pairs of pentagonal numbers that meet the requirements   
    # record the minimal difference 
    for i in range(max_n):
        for j in range(i + 1, max_n):
            p_sum  = pentagonal_nums[i] + pentagonal_nums[j]
            p_diff = pentagonal_nums[j] - pentagonal_nums[i]
            if p_sum in pentagonal_nums and p_diff in pentagonal_nums:
                if p_diff < result:
                    result = p_diff
                print("({0}, {1}): sum = {2}, diff = {3}".format(i, j, p_sum, p_diff))
    return result


def main():
    solver = Solver(solve,0)
    solver.solve()

main()

