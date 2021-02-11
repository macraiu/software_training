#include <iostream>

#include <unordered_map>

using namespace std;

int main()
{
    unordered_map<int, int> mymap;

    mymap[0] = 0;
    mymap[1] = 10;

    auto it=mymap.begin();
    for (; it!=mymap.end(); it++)
    {
        cout << "key: " << it->first << std::endl;
        cout << "value: " << it->second << std::endl;
    }
    
    return 0;

}