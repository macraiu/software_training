#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> myInts;
    int input = 0;

    while (input >= 0)
    {
        cout << "Enter number (negative to quit): " << endl;
        cin >> input;

        if (input >= 0)
        {
            myInts.push_back(input);
        }
    }

    for (auto i : myInts) 
    {
        cout << 2 * i << endl;
    }
    
    return 0;

}