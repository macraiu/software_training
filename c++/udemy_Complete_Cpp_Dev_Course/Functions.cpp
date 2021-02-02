#include <iostream>

using namespace std;


// putput = reference variable for the function
// input passed by value instead
void modifySomething1(int input, int& output)
{
    output = input + 100;
}

int main()
{

    int input = 100;
    int output;
    
    modifySomething1(input, output);
    
    cout << output << endl;

    return 0;
}