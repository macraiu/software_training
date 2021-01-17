""" 
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.

Notice that when a group of students is selected they can reorder in any possible way between themselves and the non selected students remain on their seats.

 

Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
Current array : [1,1,4,2,1,3]
Target array  : [1,1,1,2,3,4]
On index 2 (0-based) we have 4 vs 1 so we have to move this student.
On index 4 (0-based) we have 1 vs 3 so we have to move this student.
On index 5 (0-based) we have 3 vs 4 so we have to move this student.
Example 2:

Input: heights = [5,1,2,3,4]
Output: 5
Example 3:

Input: heights = [1,2,3,4,5]
Output: 0

BUBBLE SORT:
procedure bubbleSort(A : list of sortable items)
    n := length(A)
    repeat
        newn := 0
        for i := 1 to n - 1 inclusive do
            if A[i - 1] > A[i] then
                swap(A[i - 1], A[i])
                newn := i
            end if
        end for
        n := newn
    until n ≤ 1
end procedure
 """

# BUBBLE SORT - NOT GOOD FOR THIS TASK.
def heightChecker2(heights):
    print(heights)
    n = len(heights)
    swaps = 0
    while n > 0:
        newn = 0
        for i in range(1, n):
            if heights[i-1] > heights[i]:
                tmp = heights[i]
                heights[i] = heights[i-1]
                heights[i-1] = tmp
                newn = i
                swaps += 1
        n = newn
    print(heights)
    print(swaps)

def heightChecker(heights):
    sorted_heights = sorted(heights)
    counter = 0
    for n in range(len(heights)):
        if sorted_heights[n] != heights[n]:
            counter += 1

    return counter


print(heightChecker([5,1,2,3,4]))