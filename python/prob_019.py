# prob_019.py

# Problem 19
#
# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
# Bonus: How many total days were there during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
# Bonus: How many total Sundays were there during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
# Note: Strict definition of the 20th century is 1901 to 2000 inclusive. The year 1900 is in the 19th century.
#

from Solver import Solver

month_to_days = {
     1 : 31,
     2 : 28,
     3 : 31,
     4 : 30,
     5 : 31,
     6 : 30,
     7 : 31,
     8 : 31,
     9 : 30,
    10 : 31,
    11 : 30,
    12 : 31,
}

def isLeapYear(year):
    # Leap year definition
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def getDaysPerMonth(year, month):
    days = month_to_days[month] 
    # February during leap year
    if month == 2 and isLeapYear(year):
        days += 1
    return days

def getDaysPerYearUsingSum(year):
    days = 0
    for month in month_to_days:
        days += getDaysPerMonth(year, month)
    return days

def getDaysPerYear(year):
    days = 365
    if isLeapYear(year):
        days += 1
    return days

def count(start, end):
    result = 0
    for year in range(start["year"], end["year"] + 1):
        result += getDaysPerYear(year)
        # for testing
        #result += getDaysPerYearUsingSum(year)
        #print("Year {0}: {1} days".format(year, getDaysPerYear(year)))
    return result

def solveTotalDays(value):
    start = {"year" : 1901, "month" : 1,  "day" : 1 }
    end   = {"year" : 2000, "month" : 12, "day" : 31}
    result = count(start, end)
    return result

def main():
    solver = Solver(solveTotalDays, 0)
    solver.solve()

main()

