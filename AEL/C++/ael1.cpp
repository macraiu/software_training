#include <iostream>
#include <vector>
#include <map>
#include <thread>

using namespace std;


int solution(int n) {
    int d[30];
    int l = 0;
    while (n > 0) {
        d[l] = n % 2;
        n /= 2;
        l++;
    }

    cout << "l " << l << endl;

    for(int i =0;  i < l ; i++)
        cout << d[i] << endl;

    for (int p = 1; p < 1 + l/2; ++p) {
        bool ok = true;
        cout << "p " <<  p << endl; 
        for (int i = 0; i < l - p; ++i) {
            cout << " i " << i << " d[i] " << d[i] << " d[i + p] " << d[i+p] << endl;
            if (d[i] != d[i + p]) {
                ok = false;
                break;
            }
        }
        if (ok) {
            return p;
        }
    }
    return -1;
}

int main()
{


    cout << solution(955) << endl;
    //cout << solution(3003) << endl;
    //cout << solution(23) << endl;

    return 0;
}