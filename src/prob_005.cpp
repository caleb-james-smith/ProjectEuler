// prob_005.cpp

// Problem 5
// 
// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
// 
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
// 

#include <iostream>

int solve(int max_val) 
{
    int s = -1;
    int i = 1;
    bool search = true;
    while(search)
    {
        bool divisible = true;
        for (int j = 1; j < max_val + 1; ++j)
        {
            if (i % j != 0)
            {
                divisible = false;
                break;
            }
        }
        if (divisible)
        {
            search = false;
            s = i;
        }
        i += 1;
    }
    return s;
}

int main()
{
    int x = solve(20);
    std::cout << x << std::endl;
    return 0;
}

