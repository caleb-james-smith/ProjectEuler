# Easter.py

# Given a year, calculate the date of Easter that year.
# Use the fact that in 2000, Easter was on April 23, 2000.
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

# given year (yyyy), return date of Easter (yyyy-mm-dd)
def getEasterDate(year):
    date = ""
    moon_orbit = 29.53
    if year == 2000:
        date = "2000-04-23"
    return date

def main():
    print("Time to calculate the date of Easter!")

    #year = 2000
    year = int(input("Enter year: "))
    date = getEasterDate(year)
    print(f"year: {year}, date: {date}")

if __name__ == "__main__":
    main()

