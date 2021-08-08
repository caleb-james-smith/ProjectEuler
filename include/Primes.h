#ifndef PRIMES_H
#define PRIMES_H

#include <vector>

class Primes
{
private:
    std::vector<int> m_primes;
public:
    Primes();
    void setPrimes(std::vector<int> primes);
    std::vector<int> getPrimes();
};

#endif
