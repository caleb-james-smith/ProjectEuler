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
    
    const char* a1 = &value1[0];
    const char* b1 = &value2[0];
    int a = atoi(a1);
    int b = atoi(b1);
    
    std::cout << a << std::endl;
    std::cout << b << std::endl;
    int c = a + b;
    number.setValue(std::to_string(c));
    return number;
}

