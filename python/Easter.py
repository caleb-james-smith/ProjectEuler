# Easter.py

# Given a year, calculate the date of Easter that year.
# Use the fact that the first full moon in 2000 was on January 20, 2000.
# In 2000, Easter was on April 23, 2000.
# Support multiple date formats: yyyy-mm-dd and Month Day, Year.

# input: year
# output: date of Easter that year (yyyy-mm-dd)

# Examples:
#
# input: 2000
# output: 2000-04-23
#
# input: 2020
# output: 2020-04-12
#
# input: 2024
# output: 2024-03-31
#
# input: 2025
# output: 2025-04-20

# Notes:
# The reference Easter is not sufficient;
# you also need a reference full moon.
# You may want to use the precise formula for full moon dates.
# Account for leap year.
# Calculate days between two dates (if it is useful).

import datetime

# Get ordered list of full moon dates for a given year >= 2000
def getFullMoonDates(target_year):
    dates = []
    moon_orbit = 29.53
    full_moon_date = "2000-01-20"
    year = 2000
    
    # return empty list for target_year <= 2000
    if target_year < year:
        return dates
    
    # starting date
    d1 = datetime.datetime.strptime(full_moon_date, "%Y-%m-%d")
    while year <= target_year:
        # get date and year
        date = d1.strftime("%Y-%m-%d")
        year = int(d1.strftime("%Y"))
        if year == target_year:
            dates.append(date)
        # move to next date
        d2 = d1 + datetime.timedelta(days=moon_orbit)
        d1 = d2
    
    return dates

# given year (yyyy), return date of Easter (yyyy-mm-dd)
def getEasterDate(year):
    date = ""
    
    # get ordered list of full moon dates for this year
    full_moon_dates = getFullMoonDates(year)
    print(f"full_moon_dates: {full_moon_dates}")

    # return empty string if there are no full moon dates 
    if not full_moon_dates:
        return date
    
    # get date of full moon on or after equinox
    equinox_date = "{0}-03-21".format(year)
    d1 = datetime.datetime.strptime(equinox_date, "%Y-%m-%d")
    d2 = None
    full_moon_date = ""
    for full_moon_date in full_moon_dates:
        d2 = datetime.datetime.strptime(full_moon_date, "%Y-%m-%d")
        diff = d2 - d1
        if diff.days >= 0:
            full_moon_date = d2.strftime("%Y-%m-%d")
            break

    # get Sunday after full moon date
    d3 = datetime.datetime.strptime(full_moon_date, "%Y-%m-%d")
    d3 = d3 + datetime.timedelta(days=1)
    while d3.strftime("%A") != "Sunday":
        d3 = d3 + datetime.timedelta(days=1)

    date = d3.strftime("%Y-%m-%d")

    return date

def main():
    print("Time to calculate the date of Easter!")

    #year = 2000
    year = int(input("Enter year: "))
    date = getEasterDate(year)
    print(f"year: {year}, date: {date}")

if __name__ == "__main__":
    main()

