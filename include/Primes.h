#ifndef PRIMES_H
#define PRIMES_H

#include <vector>
#include <math.h>

class Primes
{
private:
    std::vector<int> m_primes;
public:
    Primes();
    void setPrimes(std::vector<int> primes);
    std::vector<int> getPrimes();
    bool divsToSqrt(int number);
    bool isPrime(int number);
    void calcPrimesBasic(int max_val);
    void calcPrimesAdvanced(int max_val);
};

#endif
