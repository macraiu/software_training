#include <iostream>
#include <string>
#include <array>

using namespace std;

int 
main()
{
    array<string, 5> names{};
    array<int, 5> weights{};

    for (int i = 0; i < 5; i++)
    {
        cout << "Name: " << endl;
        getline(cin, names[i]);

        cout << "Weight: " << endl;
        cin >> weights[i];
        cin.get();

    }

    for (int i = 0; i < 5; i++)
        cout << names[i] << " weights " << weights[i] << " lbs" << endl;

    return 0;

}