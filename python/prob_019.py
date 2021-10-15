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

DAYS_PER_WEEK   = 7
MONTHS_PER_YEAR = 12

# is a given year a leap year?
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

# get weekday (1-7) after number of days
def getNextWeekday(weekday, days):
    result = (weekday + days) % DAYS_PER_WEEK
    if result == 0:
        result = 7
    return result

# get number of days for given month; account for leap year
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

# count days from date to end of month (inclusive)
def getDaysToEndOfMonth(year, month, day):
    x = getDaysPerMonth(year, month)
    days = x - day + 1
    return days

# count days from beginning of month to date  (inclusive)
def getDaysSinceStartOfMonth(year, month, day):
    return day

# count days from date to end of year (inclusive)
def getDaysToEndOfYear(year, month, day):
    days = 0
    days += getDaysToEndOfMonth(year, month, day)
    for m in range(month + 1, MONTHS_PER_YEAR + 1):
        days += getDaysPerMonth(year, m)
    return days

# count days from beginning of year to date (inclusive)
def getDaysSinceStartOfYear(year, month, day):
    days = 0
    for m in range(1, month):
        days += getDaysPerMonth(year, m)
    days += getDaysSinceStartOfMonth(year, month, day)
    return days

# count total days between two dates (inclusive)
def countTotalDays(start, end):
    result = 0
    start_year  = start["year"]
    start_month = start["month"]
    start_day   = start["day"]
    end_year    = end["year"]
    end_month   = end["month"]
    end_day     = end["day"]
    # require end date to be on or later than start date
    if start_year > end_year:
        print("ERROR: start_year = {0}, end_year = {1}".format(start_year, end_year))
        return result
    elif start_year == end_year:
        if start_month > end_month:
            print("ERROR: start_month = {0}, end_month = {1}".format(start_month, end_month))
            return result
        elif start_month == end_month:
            if start_day > end_day:
                print("ERROR: start_day = {0}, end_day = {1}".format(start_day, end_day))
                return result
            else:
                # middle days
                x = end_day - start_day + 1
                result += x
        else:
            result += getDaysToEndOfMonth(start_year, start_month, start_day)
            result += getDaysSinceStartOfMonth(end_year, end_month, end_day)
            # middle months if any
            for month in range(start_month + 1, end_month):
                result += getDaysPerMonth(start_year, month)
    else:
        result += getDaysToEndOfYear(start_year, start_month, start_day) 
        result += getDaysSinceStartOfYear(end_year, end_month, end_day) 
        # middle years if any
        for year in range(start_year + 1, end_year):
            result += getDaysPerYear(year)
            # for testing
            #result += getDaysPerYearUsingSum(year)
            #print("Year {0}: {1} days".format(year, getDaysPerYear(year)))
    return result

# count total Sundays between two dates (inclusive)
def countTotalSundays(start, end):
    start_weekday = start["weekday"]
    total_days = countTotalDays(start, end)
    # Decrease total by current week (including Sunday)
    sunday = 7
    diff = abs(sunday - start_weekday)
    days = total_days - diff - 1
    result = (days // DAYS_PER_WEEK) + 1
    return result

# count Sundays that are on the first of the month
# assume full years are used with all months and days
def countFirstSundays(start, end):
    result  = 0
    weekday = 0
    
    start_year      = start["year"]
    start_month     = start["month"]
    start_day       = start["day"]
    start_weekday   = start["weekday"]
    end_year        = end["year"]
    end_month       = end["month"]
    end_day         = end["day"]
    end_weekday     = end["weekday"]
    
    weekday = start_weekday
    if weekday == 7:
        result += 1
    
    for year in range(start_year, end_year + 1):
        for month in range(1, MONTHS_PER_YEAR + 1):
            x = getDaysPerMonth(year, month)
            # don't use final month, as there are no more months
            if year == end_year and month == MONTHS_PER_YEAR:
                # check final weekday
                weekday = getNextWeekday(weekday, x - 1)
                if weekday == end_weekday:
                    print("PASS: final weekday is {0}; expected {1}".format(weekday, end_weekday))
                else:
                    print("FAIL: final weekday is {0}; expected {1}".format(weekday, end_weekday))
            else:
                weekday = getNextWeekday(weekday, x)
                # count Sundays
                if weekday == 7:
                    result += 1
    return result

def solve(value):
    # How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    # Weekdays: Monday (1) to Sunday (7)
    start = {"year" : 1901, "month" : 1,  "day" : 1,  "weekday" : 2}
    end   = {"year" : 2000, "month" : 12, "day" : 31, "weekday" : 7}
    #start = {"year" : 1999, "month" : 10, "day" : 10 }
    #end   = {"year" : 1999, "month" : 10, "day" : 20 }
    #result = countTotalDays(start, end)
    #result = countTotalSundays(start, end)
    result = countFirstSundays(start, end)
    return result

def main():
    solver = Solver(solve, 0)
    solver.solve()

main()

