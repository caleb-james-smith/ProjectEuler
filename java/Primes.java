// Primes.java

import java.util.Arrays;
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
    
    // Sieve of Eratosthenes
    public void calcPrimesAdvanced(int max_val)
    {
        ArrayAppend A = new ArrayAppend();
        boolean[] is_prime_list = new boolean[max_val];
        int[] primes = {};
        Arrays.fill(is_prime_list, true);
        is_prime_list[0] = false;
        is_prime_list[1] = false;
        for (int i = 2; i < (int) Math.sqrt(max_val) + 1; ++i)
        {
            if (is_prime_list[i])
            {
                for (int j = (int) Math.pow(i, 2); j < max_val; j += i)
                {
                    is_prime_list[j] = false;
                }
            }
        }
        for (int i = 0; i < is_prime_list.length; ++i)
        {
            if (is_prime_list[i])
            {
                primes = A.AppendInt(primes, i);
            }
        }
        setPrimes(primes);
    }
}

