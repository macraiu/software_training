#include <iostream>
#include <string>

using namespace std;

// base case and recursive case
// recursive case: the function has to call itself.
// recursive call
void countDownFrom(int num)
{
    if (num >= 0)
    {
        cout << num << endl;
        countDownFrom(num - 1);
    }
}

int factorial(int a);

int main()
{
    //countDownFrom(10);
    cout << factorial(6) << endl;
    return 0;

}

int factorial(int a)
{
    if (a == 1)
        //base case
        return 1;
    else
        //recursion case
        return a * factorial(a - 1);

}