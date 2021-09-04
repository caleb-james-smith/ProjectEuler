#ifndef NUMBER_H
#define NUMBER_H

#include <iostream>
#include <string>

class Number
{
private:
    std::string m_value;
public:
    Number();
    std::string getValue();
    int getLength();
    void setValue(std::string value);
    Number add(Number number);
};

#endif
