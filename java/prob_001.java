// prob_001.java

// Problem 1
// 
// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
// The sum of these multiples is 23.
// 
// Find the sum of all the multiples of 3 or 5 below 1000.
//

public class prob_001
{
    static int solve(int max_val)
    {
        int s = 0;
        for (int i = 0; i < max_val; ++i)
        {
            if (i % 3 == 0 || i % 5 == 0)
            {
                s += i;
            }
        }
        return s;
    }
    public static void main(String args[])
    {
        int x = solve(1000);
        System.out.println(x);
    }
}

