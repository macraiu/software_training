""" 
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1
 """

def countNegatives2(grid):
    # BINARY SEARCH: SLOW
    minuses = 0
    for i in grid:
        idx_start = 0
        idx_end = len(i)
        while idx_end - idx_start != 1:
            mid_idx = idx_start + (idx_end - idx_start) // 2
            if i[mid_idx] >= 0:
                idx_start = mid_idx
            else:
                idx_end = mid_idx
        
        #print(idx_start, idx_end, mid_idx)

        if i[idx_start] < 0:       
            minuses += len(i) - idx_start
        else:
            minuses += len(i) - 1 - idx_start

    return minuses

def countNegatives(grid):
    minuses = 0
    for i in grid[::-1]:
        for j in i[::-1]:
            if j < 0:
                minuses += 1
            else:
                break
    return minuses

print(countNegatives([[11]]))