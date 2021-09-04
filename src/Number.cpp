#include "../include/Number.h"

Number::Number()
{
}

std::string Number::getValue()
{
    return m_value;
}

void Number::setValue(std::string value)
{
    m_value = value;
}

Number Number::add(Number number)
{
    Number result = Number();
    
    std::string value1 = this->getValue();
    std::string value2 = number.getValue();
    std::string primary;
    std::string secondary;
    std::string answer;

    if (value1.length() >= value2.length())
    {
        printf("Use value 1 (%s) as primary\n", value1.c_str());
        primary   = value1;
        secondary = value2;
    }
    else
    {
        printf("Use value 2 (%s) as primary\n", value2.c_str());
        primary   = value2;
        secondary = value1;
    }

    // carry to next digit 
    int q = 0;
    for (int i = 0; i < primary.length(); ++i)
    {
        // get int value for each character
        int x = primary[primary.length() - 1 - i] - '0';
        int y = 0;
        if (i < secondary.length())
        {
            y = secondary[secondary.length() - 1 - i] - '0';
        }
        //std::cout << primary[primary.length() - 1 - i] << ": " << x << std::endl;
        //std::cout << secondary[secondary.length() - 1 - i] << ": " << y << std::endl;
        
        //printf("input: x = %d, y = %d, q = %d ---> ", x, y, q);
        int z = x + y + q;
        if (z > 9)
        {
            z = z - 10;
            q = 1;
        }
        else
        {
            q = 0;
        }
        //printf("output: z = %d, q = %d\n", z, q);
        answer.append(std::to_string(z));
    }
    if (q > 0)
    {
        printf("q = %d\n", q);
        answer.append(std::to_string(q));
    }
    // reverse string
    reverse(answer.begin(), answer.end());
    printf("answer: %s\n", answer.c_str());
    
    
    number.setValue(answer);
    return number;
}

