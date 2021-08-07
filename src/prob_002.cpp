// prob_002.cpp

// Problem 2
// 
// Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
// By starting with 1 and 2, the first 10 terms will be:
// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
// 
// By considering the terms in the Fibonacci sequence whose values do not exceed four million,
// find the sum of the even-valued terms.
// 

#include <iostream>

int solve(int max_val) 
{
    int s = 0;
    int x1 = 1;
    int x2 = 2;
    int x3 = x1 + x2;
    s += x2;
    while (x3 <= max_val)
    {
        if (x3 % 2 == 0)
        {
            s += x3;
        }
        x1 = x2;
        x2 = x3;
        x3 = x1 + x2;
    }
    return s;
}

int main()
{
    int x = solve(4000000);
    std::cout << x << std::endl;
    return 0;
}
