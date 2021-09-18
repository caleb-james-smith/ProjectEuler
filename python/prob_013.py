# prob_013.py
#
# Problem 13
#
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
#

from Solver import Solver

def solve(n_digits):
    data_file = "data/prob_013.txt"
    s = 0
    with open(data_file, 'r') as f:
        for line in f:
            x = line[:-1]
            if x.isdigit():
                s += int(x)
                #print(x)
    sum_string = str(s)
    answer = sum_string[:10]
    print("sum = {0}".format(s))
    print("answer = {0}".format(answer))
    return answer

def main():
    solver = Solver(solve, 10)
    solver.solve()

main()

