#include <iostream>
#include <string>
using namespace std;

#include <unordered_set>
#include "swapper.h"

#include <unordered_map>
#include <deque>
#include <stack>
#include <queue>

#include <algorithm>

template <class T>
T getBigger(T a, T b);

template <class T>
void print(T a);

template <class T>
T getSmaller(T a, T b);

typedef struct {int a; int b;} p;

typedef class printingNumbers{
    private : int a;
    private : int b;
    public : printingNumbers(int x, int y)
    {
        this->a = x;
        this->b = y;
    }

    public : void printingNums(){
        cout << "In class: " << a << " " << b << endl;
    }
} printingIntergerClass;


int main()
{
    int BiggerInt = getBigger(5,10);
    cout << BiggerInt << endl;

    int SmallerInt = getBigger(100,2-00);
    cout << SmallerInt << endl;

    print(100);
    print("Hi");
    print(3.14);

    return 0;
}

template <class T>
T getBigger(T a, T b)
{
    if(a > b)
        return a;

    return b;
}

template <class T>
T getSmaller(T a, T b)
{
    if(a < b)
        return a;

    return b;
}

template <class T>
void print(T a)
{
    cout << a << endl;
}

void CallTemplateClass()
{
    Swapper<int> IntSwapper (5,10);
    Swapper<string> StrSwapper ("John", "Mark");

    cout << IntSwapper.getFirst() << "\t" << IntSwapper.getSecond() << endl;
    cout << StrSwapper.getFirst() << "\t" << StrSwapper.getSecond() << endl;

    IntSwapper.swap();
    StrSwapper.swap();

    cout << IntSwapper.getFirst() << "\t" << IntSwapper.getSecond() << endl;
    cout << StrSwapper.getFirst() << "\t" << StrSwapper.getSecond() << endl;
}

void TypeDefClassAndStruct()
{
    p myStruct;
    myStruct.a = 100;
    myStruct.b = 1000;
    printingIntergerClass myIntClass(10, 5);
    myIntClass.printingNums();
}

void QueueSetMap()
{
        unordered_set<int> mySet;
    unordered_map<int, string> myMap;
    

    stack<int> myStack;
    myStack.push(10);
    myStack.push(5);
    myStack.push(3);
    while(!myStack.empty())
    {
        cout << "mystack " << myStack.top() << endl;
        myStack.pop();

    }

    queue<int> myQueue;
    myQueue.push(100);
    myQueue.push(10);
    myQueue.push(1);

    while(!myQueue.empty())
    {
        cout << "My queue" << myQueue.front() << endl;
        myQueue.pop();
    }

    for (int i = 0; i<5; i++)
    {
        string inp = "Here";
        mySet.insert(i);
        myMap.insert({{i, inp}});
    }
    cout << mySet.size() << endl;
    for (auto i : mySet)
    {
        cout << i << endl;
    }
    for(pair<int, string> i : myMap)
    {
        cout << i.first << endl;
        cout << i.second << endl;
    }
}