// prob_019.py
// 
// Problem 19
// 
// You are given the following information, but you may prefer to do some research for yourself.
// 
// 1 Jan 1900 was a Monday.
// Thirty days has September,
// April, June and November.
// All the rest have thirty-one,
// Saving February alone,
// Which has twenty-eight, rain or shine.
// And on leap years, twenty-nine.
// A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
// 
// How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
// 
// Bonus: How many total days were there during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
// 
// Bonus: How many total Sundays were there during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
// 
// Note: Strict definition of the 20th century is 1901 to 2000 inclusive. The year 1900 is in the 19th century.
// 

#include <iostream>
#include <string>
#include <map>

// is a given year a leap year?
bool isLeapYear(int year)
{
    // leap year definition
    if (year % 400 == 0)
    {
        return true;
    }
    else if (year % 100 == 0)
    {
        return false;
    }
    else if (year % 4 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

// get number of days for given month; account for leap year
int getDaysPerMonth(int year, int month)
{
    std::map<int,int> month_to_days;
    month_to_days[1]  = 31;
    month_to_days[2]  = 28;
    month_to_days[3]  = 31;
    month_to_days[4]  = 30;
    month_to_days[5]  = 31;
    month_to_days[6]  = 30;
    month_to_days[7]  = 31;
    month_to_days[8]  = 31;
    month_to_days[9]  = 30;
    month_to_days[10] = 31;
    month_to_days[11] = 30;
    month_to_days[12] = 31;
    int days = month_to_days[month];
    if (month == 2 and isLeapYear(year))
    {
        days += 1;
    }
    return days;
}

// get weekday (1-7) after number of days
int getNextWeekday(int weekday, int days)
{
    int result = (weekday + days) % 7;
    if (result == 0)
    {
        result = 7;
    }
    return result;
}

int test()
{
    //for(int i = 1; i < 2021; ++i)
    //{
    //    printf("year: %d", i);
    //    if (isLeapYear(i))
    //    {
    //        printf(" --- leap year");
    //    }
    //    printf("\n");
    //}
    for (int i = 1; i < 13; ++i)
    {
        int year = 1900;
        int days = getDaysPerMonth(year, i);
        printf("month: %d, days: %d\n", i, days);
    }
    return 0;
}

// count Sundays that are on the first of the month
// assume full years are used with all months and days
int countFirstSundays(std::map<std::string, int> start, std::map<std::string, int> end)
{
    int result  = 0;
    int weekday = 0;
    int start_year      = start["year"];
    int start_month     = start["month"];
    int start_day       = start["day"];
    int start_weekday   = start["weekday"];
    int end_year        = end["year"];
    int end_month       = end["month"];
    int end_day         = end["day"];
    int end_weekday     = end["weekday"];
    return result; 
}

int solve()
{
    // Weekdays: Monday (1) to Sunday (7)
    std::map<std::string, int> start;
    std::map<std::string, int> end;
    start["year"]       = 1901;
    start["month"]      = 1;
    start["day"]        = 1;
    start["weekday"]    = 2;
    end["year"]         = 2000;
    end["month"]        = 12;
    end["day"]          = 31;
    end["weekday"]      = 7;
    countFirstSundays(start, end);
    return 0;
}

int main()
{
    int x;
    x = solve();
    std::cout << "answer: " << x << std::endl;
    return 0;
}

