# prob_017.py

# Problem 17
#
# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens.
# For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.
#

from Solver import Solver

num_to_word_1 = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine"
}
num_to_word_2 = {
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
}
num_to_word_3 = {
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety",
}

def getTwoDigitWord(number):
    if number < 20:
        return num_to_word_2[number]
    a = (number // 10) * 10
    b = number % 10
    a_w = num_to_word_3[a]
    if b:
        b_w = num_to_word_1[b]
        return a_w + "-" + b_w
    else:
        return a_w

def getThreeDigitWord(number):
    a = (number // 100)
    b = number % 100
    a_w = num_to_word_1[a]
    c = a_w + " hundred"
    if b == 0:
        return c
    elif b < 10:
        b_w = num_to_word_1[b]
        return c + " and " + b_w
    else:
        b_w = getTwoDigitWord(b)
        return c + " and " + b_w

def getWord(number):
    if number < 10:
        return num_to_word_1[number]
    elif number < 100:
        return getTwoDigitWord(number)
    elif number < 1000:
        return getThreeDigitWord(number)
    elif number == 1000:
        return "one thousand"
    else:
        return ""

# count letters in word for number
# do not include spaces or hyphens
def count(number_word):
    w = number_word
    w = w.replace(" ", "")
    w = w.replace("-", "")
    return len(w)

def solve(max_val):
    result = 0
    for n in range(1, max_val + 1):
        w = getWord(n)
        c = count(w)
        print("{0} : {1} : {2}".format(n, w, c))
        result += c
    return result

def main():
    solver = Solver(solve, 1000)
    solver.solve()

main()

