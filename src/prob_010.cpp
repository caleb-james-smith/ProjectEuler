// prob_010.cpp

// Problem 10
// 
// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
// 
// Find the sum of all the primes below two million.
// 

#include <iostream>
#include "../include/Primes.h"

unsigned long long int solve(int max_val) 
{
    unsigned long long int s = 0;
    Primes P = Primes();
    P.calcPrimesAdvanced(max_val);
    std::vector<int> primes = P.getPrimes();
    for (const auto n : primes)
    {
        s += n;
    }
    return s;
}

int main()
{
    // WARNING: Use type "unsigned long long int" throughout for large numbers
    //          to avoid going past allowed max value
    unsigned long long int x;
    x = solve(2000000);
    std::cout << "answer: " << x << std::endl;
    return 0;
}

