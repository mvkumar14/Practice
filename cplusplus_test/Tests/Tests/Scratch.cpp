#include <iostream>

void PrintName(std::string& name)
{
	name = 'test' // not sure why this isn't working properly.
	std::cout << name;
}

int main()
{
	std::string firstName = "Kumar";
	std::cout << firstName;
	PrintName(firstName);
	//PrintName('test');
}

// when you have an lvalue 
// I want to check if by passing an lvalue you have
// the ability to modify the lvalue itself, instead
// of just using a temp value