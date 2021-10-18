// prob_020.py
// 
// Problem 20
// 
// n! means n × (n − 1) × ... × 3 × 2 × 1
// 
// For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
// and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
// 
// Find the sum of the digits in the number 100!
// 

#include <iostream>
#include <string>

int factorial(int number)
{
    if (number == 0 or number == 1)
    {
        return 1;
    }
    else
    {
        return number * factorial(number - 1);
    }
}

int solve(int max_val)
{
    int result = 0;
    int x = factorial(max_val);
    std::string s = std::to_string(x);
    std::cout << x << std::endl;
    for (const auto& a : s)
    {
        const char z = '0';
        int offset = int(z);
        int b = int(a) - offset;
        std::cout << a << " : " << b << std::endl;
        result += b;
    }
    return result;
}

int main()
{
    int x;
    x = solve(10);
    std::cout << "answer: " << x << std::endl;
    return 0;
}

