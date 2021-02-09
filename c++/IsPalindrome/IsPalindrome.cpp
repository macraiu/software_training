#include <iostream>
#include <string>
#include <vector>
using namespace std;

#include <memory>

bool isPalindrome(string inputString);

int main()
{
    vector<string>* StringsPtr = new vector<string>
    {
        "hello",
        "hi",
        "anna",
        "coloc",
        "ryan",
        "c"

    };

    cout << boolalpha;
    for (auto i : *StringsPtr)
    {
        cout << "The string " << i  << " is Palindrome: " << isPalindrome(i) << endl;
    }

    delete StringsPtr;
    StringsPtr = nullptr;
    
    return 0;
}

bool isPalindrome(string inputString)
{
    char* tempString = new char(inputString.size()); 
    for(auto i = inputString.end(); i != inputString.begin(); i--)
    {
        *tempString = *i;
        //tempString++;
    }

    bool isPaliindrome = (tempString == inputString);

    delete tempString;
    tempString = nullptr;

    return isPalindrome;
}