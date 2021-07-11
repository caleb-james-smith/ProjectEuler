# prob_025.py

# Problem 25
#
# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#
# Hence the first 12 terms will be:
# 
# F1  = 1
# F2  = 1
# F3  = 2
# F4  = 3
# F5  = 5
# F6  = 8
# F7  = 13
# F8  = 21
# F9  = 34
# F10 = 55
# F11 = 89
# F12 = 144
#
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
#

from Solver import Solver

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def calcFibonacci(max_val):
    values = []
    values.append(1)
    values.append(1)
    for i in range(2, max_val):
        values.append(values[i-1] + values[i-2])
    return values

def solve(parameters):
    max_val = parameters[0]
    digits  = parameters[1]
    values = calcFibonacci(max_val)
    for i in range(len(values)):
        s = str(values[i])
        num_digits = len(s)
        if num_digits == digits:
            return i + 1
    return -1

def main():
    solver = Solver(solve, [10**4, 10**3])
    solver.solve()

main()

