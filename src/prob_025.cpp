// prob_0025.cpp

// Problem 25
// 
// The Fibonacci sequence is defined by the recurrence relation:
// 
// Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
// 
// Hence the first 12 terms will be:
// 
// F1  = 1
// F2  = 1
// F3  = 2
// F4  = 3
// F5  = 5
// F6  = 8
// F7  = 13
// F8  = 21
// F9  = 34
// F10 = 55
// F11 = 89
// F12 = 144
// 
// The 12th term, F12, is the first term to contain three digits.
// 
// What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
// 

#include <iostream>
#include <vector>
#include "../include/Number.h"

int fibonacci(int n)
{
    if (n == 1 or n == 2)
    {
        return 1;
    }
    else
    {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}

std::vector<unsigned long long int> calcFibonacciInts(int max_val)
{
    std::vector<unsigned long long int> values;
    values.push_back(1);
    values.push_back(1);
    for (int i = 2; i < max_val; ++i)
    {
        values.push_back(values[i-1] + values[i-2]);
    }
    return values;
}

std::vector<Number> calcFibonacciNumbers(int max_val)
{
    std::vector<Number> values;
    Number n0 = Number();
    n0.setValue("1");
    values.push_back(n0);
    values.push_back(n0);
    for (int i = 2; i < max_val; ++i)
    {
        Number n1 = values[i-1];
        Number n2 = values[i-2];
        Number n3 = n1.add(n2);
        values.push_back(n3);
    }
    return values;
}

// example for using Number class
void example()
{
    Number n1 = Number();
    Number n2 = Number();
    std::string value1 = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111";
    std::string value2 = "999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999";
    //std::string value1 =  "999";
    //std::string value2 = "111";
    //std::string value1 =  "456";
    //std::string value2 = "1230";
    n1.setValue(value1);
    n2.setValue(value2);
    Number n3 = n1.add(n2);
    std::cout << "n1 = " << n1.getValue() << std::endl;
    std::cout << "n2 = " << n2.getValue() << std::endl;
    std::cout << "n3 = " << n3.getValue() << std::endl;
}

int solve(int max_val, int target_digits) 
{
    // example for using Number class
    //example();
    
    // works for small numbers
    // limited by storage size of "unsigned long long int"
    //std::vector<unsigned long long int> values = calcFibonacciInts(max_val);
    //for (int i = 0; i < values.size(); ++i)
    //{
    //    std::string val_str = std::to_string(values[i]);
    //    int num_digits = val_str.size();
    //    printf("%d: %llu ---> %d digits\n", i, values[i], num_digits);
    //    if (num_digits == target_digits)
    //    {
    //        return i + 1; 
    //    }
    //}
    
    // works for large numbers
    std::vector<Number> values = calcFibonacciNumbers(max_val);
    for (int i = 0; i < values.size(); ++i)
    {
        int num_digits = values[i].getLength();
        //printf("%d: %s ---> %d digits\n", i, values[i].getValue().c_str(), num_digits);
        if (num_digits == target_digits)
        {
            printf("%s\n", values[i].getValue().c_str());
            printf("number of digits: %d\n", num_digits);
            return i + 1; 
        }
    }
    
    return -1;
}

int main()
{
    int x = solve(10000, 1000);
    printf("answer: %d\n", x);
    return 0;
}

