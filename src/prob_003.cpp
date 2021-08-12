// prob_003.cpp

// Problem 3
// 
// The prime factors of 13195 are 5, 7, 13 and 29.
// 
// What is the largest prime factor of the number 600851475143 ?
// 

#include <iostream>
#include "../include/Primes.h"

// get prime factors of a number
// use list of primes to improve speed
std::vector<int> primeFactors(long long int number, std::vector<int> primes)
{
    std::vector<int> prime_factors;
    int i = 0;
    while (i < primes.size() and primes[i] <= number)
    {
        if (number % primes[i] == 0)
        {
            prime_factors.push_back(primes[i]);
        }
        i += 1;
    }
    return prime_factors;
}

int solve(long long int number) 
{
    int max_val = 10000;
    int s = 0;
    Primes P = Primes();
    P.calcPrimesBasic(max_val);
    std::vector<int> primes = P.getPrimes();
    //std::cout << "-----" << std::endl;
    //for (const auto num : primes)
    //{
    //    std::cout << num << std::endl;
    //}
    //std::cout << "-----" << std::endl;
    std::cout << "Number of primes less than " << max_val << ": " << primes.size() << std::endl;
    std::vector<int> prime_factors = primeFactors(number, primes);
    std::cout << "factors: ";
    for (const auto num : prime_factors)
    {
        std::cout << num << ", ";
    }
    std::cout << std::endl;
    s = prime_factors.back();
    return s;
}

int main()
{
    // WARNING: Use type "long long int" throughout for large number
    //          to fix "Segmentation fault: 11" that occurs for large values.
    long long int x;
    x = solve(13195);
    std::cout << "answer: " << x << std::endl;
    x = solve(600851475143);
    std::cout << "answer: " << x << std::endl;
    return 0;
}

