#include "../include/Primes.h"

Primes::Primes()
{
}

void Primes::setPrimes(std::vector<int> primes)
{
    m_primes = primes;
}

std::vector<int> Primes::getPrimes()
{
    return m_primes;
}

bool Primes::divsToSqrt(int number)
{
    int i = 2;
    while (i <= int(sqrt(number)))
    {
        if (number % i == 0)
        {
            return true;
        }
        i += 1;
    }
    return false;
}

bool Primes::isPrime(int number)
{
    if (number == 1)
    {
        return false;
    }
    return not divsToSqrt(number);
}

void Primes::calcPrimesBasic(int max_val)
{
    std::vector<int> primes;
    for (int i = 1; i < max_val; ++i)
    {
        if (isPrime(i))
        {
            primes.push_back(i);
        }
    }
    setPrimes(primes); 
}

// Sieve of Eratosthenes
void Primes::calcPrimesAdvanced(int max_val)
{
    std::vector<bool> is_prime_list(max_val, true);
    std::vector<int>  primes;
    is_prime_list[0] = false;
    is_prime_list[1] = false;
    for (int i = 2; i < int(sqrt(max_val)) + 1; ++i)
    {
        if (is_prime_list[i])
        {
            for (int j = pow(i, 2); j < max_val; j += i)
            {
                is_prime_list[j] = false;
            }
        }
    }
    for (int i = 0; i < is_prime_list.size(); ++i)
    {
        if (is_prime_list[i])
        {
            primes.push_back(i);
        }
    }
    setPrimes(primes); 
}

