#include <iostream>
#include <vector>
using namespace std;

int removeDuplicates(vector<int>& nums) {
    
    auto i = nums.begin() + 1;

    while(i < nums.end())
    {
        if(*i == *(i-1))
            nums.erase(i);
        else
            i++;
    }

    return nums.size();
}

int main()
{
    vector<int> nums;
    cout << "is empty: " << boolalpha << nums.empty() << endl;      

    cout << removeDuplicates(nums) << endl;

    for(auto i : nums)
        cout << i << " ";

    return 0;
}