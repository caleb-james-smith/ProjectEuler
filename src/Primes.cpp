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

