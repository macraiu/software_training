/********************************************************************************************************
    Given a string cormed by 'a' and 'b' characters, how many ways the string can be split in 3 segments each
    containing the same number of 'a' characters.
*********************************************************************************************************/

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int solution(string &S) {

    int a = count(S.begin(), S.end(), 'a');
    if (a == 0)
    {
        return (S.size() - 1) * (S.size() - 2) / 2; 
    }

    if (a % 3 != 0)
    {
        return 0;
    }

    int count = 0;
    int first_b = 0;
    int second_b = 0;
    
    for(auto i : S)
    {
        if(count == a / 3)
        {
            first_b += 1;
        }
        if(count == 2 * a /3 )
        {
            second_b += 1;
        }

        if(i == 'a')
        {
            count += 1;
        }

    }
    
    return first_b * second_b;
}


int main()
{
    string s = "abbabba";
    cout << solution(s) << endl;
    return 0;
}