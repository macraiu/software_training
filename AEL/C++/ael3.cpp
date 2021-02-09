/*******************************************************************************************************
    Given an array such as A[0,9,0,2,6,8,0,8,3,0] with N elements (cities) and N-1 edges (routes),
    where the each A[i] and i represent an edge, which is the maximum number of cities can be visited
    starting from the city number 0, passing by only one odd city ?
********************************************************************************************************/

#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <set>

using namespace std;

void findPaths(multimap<int,int> myMap, vector<unordered_set<int>>& paths, unordered_set<int> path, int idx)
{

    int to_remove;
    auto range = myMap.equal_range(idx);
    for(auto it = range.first; it != range.second; ++it)
    {
        if(path.count(it->second) == 0)
        {
            path.insert(it->second);
            findPaths(myMap, paths, path, it->second);
            path.erase(it->second);
        }
    }
    paths.push_back(path);

}

void createEdges(vector<int> &T, multimap<int,int>& myMap)
{
    for(auto i = T.begin() + 1; i!= T.end(); i++)
    {
        myMap.insert(pair<int, int>(*i, i - T.begin()));
        myMap.insert(pair<int, int>(i - T.begin(), *i));
    }

}

int validatePath(unordered_set<int> path)
{
    int odds = 0;
    for(auto city: path)
    {
        if(city % 2 == 1)
        {
            odds += 1;
        }   
        if(odds == 2)
        {
            return -1;
        }
    }
    return path.size();

}

int solution(vector<int> &T) {

    multimap<int,int> myMap;
    createEdges(T, myMap);

    vector<unordered_set<int>> paths;
    unordered_set<int> path;
    path.insert(0);
    findPaths(myMap, paths, path, 0);

    set<int> validPathLengths;
    int length;
    for(auto path : paths)
    {
        length = validatePath(path);
        if(length != -1)
        {
            validPathLengths.insert(length);
        }
    }

    return *validPathLengths.end();
}

int main()
{
    vector<int> T{0,9,0,2,6,8,0,8,3,0};
    cout << solution(T) << endl;
    return 0;
}