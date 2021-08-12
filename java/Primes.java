// Primes.java

import java.lang.Math;

public class Primes
{
    int[] m_primes;
    public void setPrimes(int[] primes)
    {
        m_primes = primes;
    }
    public int[] getPrimes()
    {
        return m_primes;
    }
    public boolean divsToSqrt(int number)
    {
        int i = 2;
        while (i <= (int) Math.sqrt(number))
        {
            if (number % i == 0)
            {
                return true;
            }
            i += 1;
        }
        return false;
    }
    public boolean isPrime(int number)
    {
        if (number == 1)
        {
            return false;
        }
        return ! divsToSqrt(number); 
    }
    public void calcPrimesBasic(int max_val)
    {
        ArrayAppend A = new ArrayAppend();
        int[] primes = {};
        for (int i = 1; i < max_val; ++i)
        {
            if (isPrime(i))
            {
                primes = A.AppendInt(primes, i);
            }
        }
        setPrimes(primes);
    }
}

