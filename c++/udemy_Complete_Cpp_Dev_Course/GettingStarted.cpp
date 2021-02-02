/*
    C++ Developer course
    Author: Craiu Muller Martin

*/


#include <iostream>
#include <string>
#include <array>
#include <time.h>
#include <vector>


using namespace std;


// entry point of the application
int 
main()
{

    // // BUILD IN C/TYPE ARRAYS
    // int a[10]{10, 100, 1000};

    // for(auto i : a)
    // {
    //     cout << i << endl;
    // }

    // string names[]{"ann", "james", "john"};start
    // array<int, 5> myIntArray{};
    // for(auto ints : myIntArray)
    // {
    //     cout << ints << endl;
    // }

    // myIntArray[2] = 100;
    // cout << myIntArray.size() << endl;
    // myIntArray.fill(5); 

    // for(auto i : myIntArray)
    // {
    //     cout << i << endl;
    // }

    // for populating you use a regular for loop
    // for printing you can use the shorthand

    // vector is dynamically rearranging its size
    vector<string> anotherVec;
    anotherVec.push_back("hi");
    anotherVec.push_back("my");
    anotherVec.push_back("name");
    anotherVec.push_back("is");
    anotherVec.push_back("martin");

    cout << "vec size" << anotherVec.size() << endl;

    for (auto i : anotherVec)
    {
        cout << " " << i ;
    }
    cout << endl;

    anotherVec.pop_back();
    auto one_vec = anotherVec.rend();

    anotherVec.insert(anotherVec.begin() + 1 , "Hello");
    anotherVec.push_back("Mark");

    for( auto elements : anotherVec)
    {
        cout << elements << endl;
    }


    // 2D ARRAY
    int my2darray[2][3]{
        {1,2,3},
        {4,5,6}     
    };

    // nested loop if you have to print out all the elements
    for (int i = 1; i >= 0; i--)
    {
        for (int j = 2; j >= 0; j--)
        {
            cout << my2darray[i][j] << " ";
        }
        cout << endl;
    }

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cout << my2darray[i][j] << " ";
        }
        cout << endl;
    }


    // int myInt = 15;
    // char singleChar = 'a'; // Comment
    // string myName = "Martin";
    // bool isRaining = false;
    // bool isSunny = !isRaining;
    // // c++ is considered false = 0 and true = 1 
    // double myDouble = 3.14;
    // double tax = 0.06;
    // const double pi = 3.14;

    // int *p = &myInt;
    // cout << "pointer content: " << p << endl;
    // cout << "content of what pointer is pointing: " << *p << endl;
    // cout << "content of what pointer is pointing incremented: " << *p++ << endl;
    // cout << "myint " << myInt << endl;
    // cout << "content of what pointer is pointing incremented: " << p << endl;
    // cout << "Hello " << "John" << endl;
    // cout << "My var: " << myInt << endl;
    // cout << "Double number:" << myDouble << endl;
    // cout << "Single char: " << singleChar << endl;
    // cout << "My name: " << myName << endl;
    // cout << "My bool: " << isRaining << endl;
    // cout << boolalpha;
    // // bools are wirtten in alphanumeric
    // cout << "My bool text: " << isRaining << endl;
    // // use to print out the actual text of true or false
    
    // // logical operators  ! not, && and, || or    over booleans
    // // unary operator &, |,  btiwise operations
    // // ternary operator 

    // // obtain data from outside
    // // keyboad input

    // int Age;
    // string Name;



    // cout << "Enter your age: " << endl;
    // cin >> Age;
    // cout << "Echo Your age: " << Age << endl;

    // // consume the end of line character 
    // cin.get();
    // // not gonna catch it, but we consume the end of line character.

    // cout << "Enter your Name: " << endl;
    // // cin >> Name;
    // // not good if there are spaces
    // getline(cin, Name); // first arg is source of data, second 

    // cout << "Echo Your Name: " << Name << endl;


    // char grade;
    // bool stay = true;

    // while(stay)
    // {
    //     cout << "Enter yor your grade: " << endl;
    //     cin >> grade;
    //     switch(grade)
    //     {
    //         case 'A':
    //         case 'a':
    //             cout << "Excellent!" << endl;
    //             break;
    //         case 'B':
    //         case 'b':
    //             cout << "Good!" << endl;
    //             break;
    //         case 'C':
    //         case 'c':
    //             cout << "Can do better!" << endl;
    //             break;
    //         case 'D':
    //         case 'd':
    //             cout << "Careful to not fail the course!" << endl;
    //             break;
    //         case 'F':
    //         case 'f':
    //             cout << "Course failed" << endl;
    //             break;
    //         default:
    //             cout << "Not a valid grade" << endl;
    //             stay = false;
    //             break;
    //     }
    // }    

    // return 0;


    // //random numbers
    // srand(time(nullptr));

    // int dieValue = rand() % 10 + 1;

    // from [0 to 10) shifted by 1, so from [1 to 10]


}