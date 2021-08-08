// prob_003.cpp

// Problem 3
// 
// The prime factors of 13195 are 5, 7, 13 and 29.
// 
// What is the largest prime factor of the number 600851475143 ?
// 

#include <iostream>
#include "../include/Primes.h"

int solve(int max_val) 
{
    // input array 
    int input[] = {2, 3, 5};
    std::vector<int> vec(std::begin(input), std::end(input));
    for (const auto num : vec)
    {
        std::cout << num << std::endl;
    }
    Primes P = Primes();
    P.setPrimes(vec);
    std::vector<int> primes = P.getPrimes();
    for (const auto num : primes)
    {
        std::cout << num << std::endl;
    }
    int s = 0;
    return s;
}

int main()
{
    int x = solve(99);
    std::cout << x << std::endl;
    return 0;
}

