// prob_006.java

// Problem 6
// 
// The sum of the squares of the first ten natural numbers is 385.
// 
// The square of the sum of the first ten natural numbers is 3025.
// 
// Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640.
// 
// Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
// 

import java.lang.Math;

public class prob_006
{
    static int solve(int max_val)
    {
        int answer = 0;
        int sum    = 0;
        int sum_of_squares = 0;
        int square_of_sum  = 0;
        for (int i = 1; i < max_val + 1; ++i)
        {
            sum += i;
            sum_of_squares += (int) Math.pow(i, 2);
        }
        square_of_sum = (int) Math.pow(sum, 2);
        answer = square_of_sum - sum_of_squares;
        return answer;
    }
    public static void main(String args[])
    {
        int x = solve(100);
        System.out.println(x);
    }
}

