#include <iostream>
#include <algorithm>
#include <array>
#include <vector>


using namespace std;

int main ()
{
    vector<int> *vectorPtr = new vector<int>;
    vectorPtr->push_back(100);
    vectorPtr->push_back(10);
    vectorPtr->push_back(5);
    vectorPtr->push_back(1);

    int countsOfFives = count(vectorPtr->begin(), vectorPtr->end(), 5);
    replace(vectorPtr->begin(), vectorPtr->end(), 5, 99);

    cout << "fives: " << countsOfFives << endl;

    for(auto it = vectorPtr->rbegin(); it != vectorPtr->rend(); ++it)
    {
        cout << *it << endl;
    }

    delete vectorPtr;
    vectorPtr = nullptr;

    return 0;
}