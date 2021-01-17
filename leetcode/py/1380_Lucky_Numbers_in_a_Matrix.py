""" 
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
 """

def luckyNumbers2(matrix):
    min_set = set()
    max_set = set()

    for i in matrix:
        min_set.add(min(i))
    for j in zip(*matrix):
        max_set.add(max(j))

    return [min_set & max_set]

def luckyNumbers (matrix):
    print(matrix)
    print(*matrix)
    return list(set(min(i) for i in matrix) & set(max(i) for i in zip(*matrix)))



print(luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))

*a, = 'ciao'
print(a)