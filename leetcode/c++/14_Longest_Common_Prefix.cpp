#include <iostream>
#include <vector>
#include <string>

using namespace std;

string longestCommonPrefix(vector<string>& strs) {

    if (strs.size() == 0) return "";
    if (strs.size() == 1) return strs[0];
    
    vector<char> letters;
    for(int j = 0; j < strs[0].size(); j++)
    {
        for(int i = 1; i < strs.size(); i++)
        {
            if(strs[i][j] != strs[i-1][j])
            {
                string s(letters.begin(), letters.end());
                return s;
            }
        }
        letters.push_back(strs[0][j]);
    }

    string s(letters.begin(), letters.end());
    return s;

}

int main()
{
    vector<string> myStrings{"Hal", "Hal", "Ha"};

    cout << longestCommonPrefix(myStrings) << endl;

    return 0;
}