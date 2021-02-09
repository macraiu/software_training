#include <iostream>
#include <vector>

using namespace std;

vector<int> plusOne(vector<int>& digits) {
    
    for(auto i = digits.rbegin(); i != digits.rend() ; i++)
    {
        cout << "*i " << *i << endl;
        *i += 1;
        if(*i == 10)
            *i = 0;
        else
            return digits;
        
    }

    digits.insert(digits.begin(), 1);
    return digits;

}

int main()
{
    vector<int> digits{0,0};
    plusOne(digits);
    
    for(auto i : digits)
    {
        cout << i << " ";
    }
    cout << endl;
    
    return 0;
}