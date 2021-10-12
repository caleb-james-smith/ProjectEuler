// prob_013.cpp

// Problem 13
// 
// Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
// 

#include <iostream>
#include <fstream>
#include <string>
#include "../include/Number.h"

std::string solve(int n_digits) 
{
    Number s = Number();
    s.setValue("0");
    std::string file_name = "data/prob_013.txt";
    std::ifstream data_file(file_name);
    std::string text;
    while(std::getline(data_file, text))
    {
        //std::cout << text << std::endl;
        Number x = Number();
        x.setValue(text);
        s = s.add(x);
    }
    std::string answer = s.getValue().substr(0, 10);
    std::cout << "sum = " << s.getValue() << std::endl;
    std::cout << "answer = " << answer << std::endl;
    return answer;
}

int main()
{
    std::string x = solve(10);
    std::cout << "answer: " << x << std::endl;
    return 0;
}

