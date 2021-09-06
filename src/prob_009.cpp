// prob_009.cpp

// Problem 9
// 
// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
// 
// a^2 + b^2 = c^2
// 
// For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
// 
// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// 
// Find the product abc.
// 

#include <iostream>
#include <math.h>

bool isTriplet(int a, int b, int c)
{
    return pow(a, 2) + pow(b, 2) == pow(c, 2);
}

int solve(int target_val) 
{
    int result = -1;
    int max_val_a = target_val / 3;
    int max_val_b = target_val / 2;
    for (int a = 1; a < max_val_a; ++a)
    {
        for (int b = a + 1; b < max_val_b; ++b)
        {
            // require "a + b + c = target value" to eliminate loop over "c"
            int c = target_val - a - b;
            if (isTriplet(a, b, c))
            {
                int s = a + b + c;
                int p = a * b * c;
                printf("(a, b, c): (%d, %d, %d), sum = %d, product = %d\n", a, b, c, s, p);
                result = p;
                return result;
            }
        }
    }
    return result;
}

int main()
{
    int x = solve(1000);
    std::cout << x << std::endl;
    return 0;
}

