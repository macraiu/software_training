#include <iostream>
#include <array>

using namespace std;

int trialFunctionPtr(int a)
{
    return a * 10;
}

int main()
{
    int myInt = 100;
    int* myIntPtr = &myInt;

    cout << *myIntPtr << endl;

    // RAW pointer
    bool* boolPtr = new bool(false);
    *boolPtr = true;
    cout << boolalpha << *boolPtr << endl;

    delete boolPtr;

    boolPtr = nullptr;

    int dim;
    cout << "give dimensions";
    cin >> dim;

    array<int, dim> a;
    cout <<  << endl;
    cout << a[1] << endl;


    return 0;
}