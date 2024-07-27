# prob_001.py

# Problem 1
#
# Multiples of 3 or 5
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#

def solve(max_val):
    s = 0
    for i in range(1, max_val):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s

x = solve(1000)
print(x)

