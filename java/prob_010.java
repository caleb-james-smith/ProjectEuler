// prob_010.cpp

// Problem 10
// 
// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
// 
// Find the sum of all the primes below two million.
// 

import java.util.Arrays;

public class prob_010
{
    static long solve(int max_val)
    {
        long s = 0;
        Primes P = new Primes();
        P.calcPrimesAdvanced(max_val);
        int[] primes = P.getPrimes();
        for (int n: primes)
        {
            s += n;
        }
        return s;
    }
    public static void main(String args[])
    {
        // WARNING: Use type "long" for large numbers 
        //          to avoid going past allowed max value
        long x;
        x = solve(2000000);
        System.out.println("answer: " + x);
    }
}

