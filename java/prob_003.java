// prob_003.java

// Problem 3
// 
// The prime factors of 13195 are 5, 7, 13 and 29.
// 
// What is the largest prime factor of the number 600851475143 ?
// 

import java.util.Arrays;

public class prob_003
{
    static int[] primeFactors(long number, int[] primes) 
    {
        ArrayAppend A = new ArrayAppend();
        int[] prime_factors = {};
        int i = 0; 
        while(i < primes.length && primes[i] <= number)
        {
            if (number % primes[i] == 0)
            {
                prime_factors = A.AppendInt(prime_factors, primes[i]);
            }
            i += 1;
        }
        return prime_factors;
    }
    static int solve(long number)
    {
        int max_val = 10000;
        int s = 0;
        Primes P = new Primes();
        P.calcPrimesBasic(max_val);
        int[] primes = P.getPrimes();
        int[] prime_factors = primeFactors(number, primes);
        //System.out.println(Arrays.toString(primes));
        System.out.println("Number of primes less than " + max_val + ": " + primes.length);
        System.out.println("factors: " + Arrays.toString(prime_factors));
        s = prime_factors[prime_factors.length - 1];
        return s;
    }
    public static void main(String args[])
    {
        // WARNING: Use type "long" and append L to large number: 600851475143L
        //          to avoid "error: integer number too large" error.
        int x = solve(13195);
        System.out.println("answer: " + x);
        x = solve(600851475143L);
        System.out.println("answer: " + x);
    }
}

