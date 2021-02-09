#include <iostream>
#include <vector>

using namespace std;

int singleNumber(vector<int>& nums) {
    
    int x = 0;
    for(auto i: nums)
        x ^= i;
    return x;

}

int main()
{
    vector<int> nums{2,2,1,1,5,4,4};
    cout << singleNumber(nums) << endl;

    return 0;
}